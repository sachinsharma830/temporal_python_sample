import asyncio
import concurrent.futures
import logging
from temporalio.client import Client
from temporalio.worker import Worker

# Import the activity and workflow from our other files
from activites.activities import get_ip_address, say_hello
from workflow.workflows import IPAddress, SayHello

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    try:
        # Create client connected to server at the given address
        logger.info("Connecting to Temporal server at localhost:7233")
        client = await Client.connect("localhost:7233")
        logger.info("Connected to Temporal server")

        # Run the worker
        logger.info("Starting worker")
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=100
        ) as activity_executor:
            worker = Worker(
                client,
                task_queue="my-task-queue",
                workflows=[IPAddress, SayHello],
                activities=[get_ip_address, say_hello],
                activity_executor=activity_executor
            )
            await worker.run()
        logger.info("Worker stopped")

    except Exception as e:
        logger.error(f"Error running worker: {e}")


if __name__ == "__main__":
    asyncio.run(main())
