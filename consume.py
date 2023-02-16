import asyncio

from aio_pika import connect
from aio_pika.abc import AbstractIncomingMessage
from app.mongodb import insert_data


async def on_message(message: AbstractIncomingMessage) -> None:
    """
    on_message doesn't necessarily have to be defined as async.
    Here it is to show that it's possible.
    """
    print("Message body is: %r" % message.body.decode())
    print("Before sleep!")
    resource = insert_data(message.body.decode())
    print(f" result!!! {resource}")
    await asyncio.sleep(5)  # Represents async I/O operations
    print("After sleep!")


async def main() -> None:
    connection = await connect("amqp://guest:guest@rabbitmq:5672/")
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("connecting")
        await queue.consume(on_message, no_ack=True)
        print(" [*] Waiting for messages. To exit press CTRL+C")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
