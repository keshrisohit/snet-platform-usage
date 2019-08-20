from models import UserOrgGroupModel, UsageModel
from repository.org_service_config_repository import OrgServiceRepo
from repository.usage_repository import UsageRepository
from repository.user_org_group_repository import UserOrgGroupRepository


class Storage(object):

    # Interface to raad write data fom cache or database

    def add_usage_data(self, usage_detail):
        pass

    def get_usage_details(self, username, org_id, service_id, group_id=None):
        pass


class DatabaseStorage(Storage):
    usage_repo = UsageRepository()
    org_service_config_repo = OrgServiceRepo()
    user_org_group_repo = UserOrgGroupRepository()

    def get_user_org_group(self, usage_details):
        user_org_group_repo_data = self.user_org_group_repo.get_user_org_group_data(
            payment_group_id=usage_details["group_id"],
            org_id=usage_details["organization_id"],
            user_name=usage_details["username"],
            service_id=usage_details["service_id"],
            resource=usage_details["service_method"]
        )

        return user_org_group_repo_data

    def add_usage_data(self, usage_details):
        existing_user_org_group_repo_data = self.get_user_org_group(
            usage_details)

        if existing_user_org_group_repo_data is None:
            print("existing_user_org_group_repo_data is None")
            new_user_org_record = UserOrgGroupModel(
                payment_group_id=usage_details["group_id"],
                org_id=usage_details["organization_id"],
                user_name=usage_details["username"],
                service_id=usage_details["service_id"],
                resource=usage_details["service_method"]
            )
            self.user_org_group_repo.create_item(new_user_org_record)

        user_org_group_repo_data = self.get_user_org_group(usage_details)
        user_org_group_id = user_org_group_repo_data.id
        usage_record = UsageModel(
            client_type=usage_details['client_type'],
            ethereum_json_rpc_endpoint=usage_details['ethereum_json_rpc_endpoint'],
            registry_address_key=usage_details['registry_address_key'],
            user_org_group_id=user_org_group_id,
            status=usage_details['status'],
            start_time=usage_details['start_time'],
            end_time=usage_details['end_time'],
            response_time=usage_details['response_time'],
            response_code=usage_details['response_code'],
            error_message=usage_details['error_message'],
            version=usage_details['version'],
            channel_id=usage_details['channel_id'],
            operation=usage_details['operation'],
            group_id=usage_details["group_id"],
            org_id=usage_details["organization_id"],
            usage_type=usage_details['usage_type'],
            usage_value=usage_details['usage_value'],
            user_details=usage_details['user_details'],
            user_name=usage_details["username"],
            service_id=usage_details["service_id"],
            resource=usage_details["service_method"],
            request_id=usage_details["request_id"],

        )
        self.usage_repo.create_item(usage_record)

    def get_usage_details(self, user_name, org_id, service_id, group_id=None):
        optin_time = self.usage_repo.get_optin_time(
            user_name, org_id, service_id)
        free_calls = self.org_service_config_repo.get_service_config(
            org_id, service_id, optin_time)
        total_calls = self.usage_repo.get_total_calls(
            user_name, org_id, service_id)
        return total_calls, free_calls
