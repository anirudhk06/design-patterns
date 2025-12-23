from abc import ABC, abstractmethod


class ComputeService(ABC):
    @abstractmethod
    def start_instance(self):
        raise NotImplementedError(
            "subclasses must be implement start_instance() method"
        )

    @abstractmethod
    def stop_instance(self):
        raise NotImplementedError("subclasses must be implement stop_instance() method")


class StorageService(ABC):
    @abstractmethod
    def upload_file(self):
        raise NotImplementedError("subclasses must be implement upload_file() method")

    @abstractmethod
    def download_file(self):
        raise NotImplementedError("subclasses must be implement download_file() method")


class AWSComputeService(ComputeService):
    def start_instance(self):
        print("Instance starting")

    def stop_instance(self):
        print("Instang stopped")


class AWSStorageService(StorageService):
    def upload_file(self):
        print("Uploading the file")

    def download_file(self):
        print("Downloading the file")


class GCPComputeService(ComputeService):
    def start_instance(self):
        print("Instance starting")

    def stop_instance(self):
        print("Instang stopped")


class GCPStorageService(StorageService):
    def upload_file(self):
        print("Uploading the file")

    def download_file(self):
        print("Downloading the file")


class CloudProviderInterface(ABC):
    @abstractmethod
    def create_compute_service(self):
        raise NotImplementedError(
            "subclasses must be implement create_compute_service() method"
        )

    @abstractmethod
    def create_storage_service(self):
        raise NotImplementedError(
            "subclasses must be implement create_storage_service() method"
        )


class AWSFactory(CloudProviderInterface):
    def create_compute_service(self) -> ComputeService:
        return AWSComputeService()

    def create_storage_service(self) -> StorageService:
        return AWSStorageService()


class GCPFactory(CloudProviderInterface):
    def create_compute_service(self) -> ComputeService:
        return GCPComputeService()

    def create_storage_service(self) -> StorageService:
        return GCPStorageService()


def main() -> None:
    factory = AWSFactory()
    compute = factory.create_compute_service()
    storage = factory.create_storage_service()
    compute.start_instance()
    compute.stop_instance()

    storage.upload_file()
    storage.download_file()


if __name__ == "__main__":
    main()
