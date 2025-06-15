from typing import Any
import threading
from queue import Queue, Empty


class SingletonMeta(type):
    _instance = None
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs) -> Any:
        if cls._instance is None:
            with cls._lock:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class ConnectionPoolManager(metaclass=SingletonMeta):
    def __init__(self, pool_size: str | int = 1) -> None:
        self._pool = Queue(maxsize=pool_size)
        self._all_connections = set()

        for i in range(pool_size):
            conn = f"conn-{i+1}"
            self._pool.put(conn)
            self._all_connections.add(conn)

    def get_connection(self) -> Any:
        try:
            return self._pool.get_nowait()
        except Empty:
            raise RuntimeError("No connections available")

    def release_connection(self, conn: str) -> None:
        if conn not in self._all_connections:
            raise ValueError(f"Invalid connection: {conn}")

        self._pool.put_nowait(conn)

    def available(self) -> int:
        return self._pool.qsize()

    def total(self) -> int:
        return len(self._all_connections)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
