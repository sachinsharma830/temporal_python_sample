from datetime import timedelta
from temporalio import workflow

from params.params import APIParams

# Import our activity, passing it through the sandbox
with workflow.unsafe.imports_passed_through():
    from activites.activities import say_hello, get_ip_address


@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            say_hello, name, schedule_to_close_timeout=timedelta(seconds=5)
        )


@workflow.defn
class IPAddress:
    @workflow.run
    async def run(self, api_params: APIParams) -> str:
        return await workflow.execute_activity(
            get_ip_address, api_params, schedule_to_close_timeout=timedelta(seconds=5)
        )
