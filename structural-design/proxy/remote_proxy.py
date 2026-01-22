from abc import ABC, abstractmethod


class UserService(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> dict:
        pass


class RemoteUserService(UserService):
    def get_user(self, user_id: str) -> dict:
        import random, time

        print(f"[REMOTE] Calling remote service for user {user_id}")
        time.sleep(1)

        if random.choice([True, False]):
            raise Exception("Network error")

        return {"id": user_id, "name": "Anirudh k"}


class UserServiceProxy(UserService):
    def __init__(self, service: UserService, retries: int = 3):
        self._service = service
        self._retries = retries

    def get_user(self, user_id: int):
        print(f"[PROXY] Requesting user {user_id}")

        last_exception = None

        for attempt in range(1, self._retries + 1):
            try:
                result = self._service.get_user(user_id)
                if attempt > 1:
                    print(f"[PROXY] Success on attempt {attempt}")

                return result
            except Exception as e:
                last_exception = e
                print(f"[PROXY] Attempt {attempt} failed: {e}")

        print("[PROXY] All retries failed")
        raise last_exception


def main() -> None:
    service = UserServiceProxy(RemoteUserService())
    print(service.get_user(10))


if __name__ == "__main__":
    main()
