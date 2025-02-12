import asyncio
import logging
import uuid

from temporalio.client import Client

from params.params import APIParams

# Import the workflow from the previous code
from workflow.workflows import SayHello
from workflow.workflows import IPAddress

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    try:
        # Create client connected to server at the given address
        logger.info("Connecting to Temporal server at localhost:7233")
        client = await Client.connect("localhost:7233")
        logger.info("Connected to Temporal server")

        # Execute a workflow
        logger.info("Executing SayHello workflow")
        result = await client.execute_workflow(
            SayHello.run, "my name", id="my-workflow-id", task_queue="my-task-queue"
        )
        logger.info(f"SayHello workflow result: {result}")

        logger.info("Executing IPAddress workflow")
        api_params = APIParams(chapter=1, verse=2)
        result = await client.execute_workflow(
            IPAddress.run, api_params, id="my-workflow-id", task_queue="my-task-queue"
        )
        logger.info(f"IPAddress workflow result: {result}")

    except Exception as e:
        logger.error(f"Error executing workflow: {e}")


if __name__ == "__main__":
    asyncio.run(main())
