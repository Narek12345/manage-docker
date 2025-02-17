import docker


client = docker.from_env()

environment  = {
	"TELEGRAM_BOT_TOKEN": "",
}

container = client.containers.run(
	"telegram_bot",
	name="telegram_bot",
	detach=True,
	environment=environment,
)
