install:
	pip install -r requirements.txt
	useradd ssbu_discord_bot -d $(CURDIR)
	chown ssbu_discord_bot:ssbu_discord_bot . -R
	ln -s $(CURDIR)/ssbu_discord_bot.service /etc/systemd/system
	systemctl daemon-reload
	systemctl enable ssbu_discord_bot.service
	systemctl restart ssbu_discord_bot.service


