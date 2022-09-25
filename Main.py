from datetime import datetime
from AMF import AMF
from SessionID import SessionID
import discord
from pyamf import remoting
from discord.ext import commands
from discord import app_commands
from SessionThread import myThread, myThread1

from TicketGenerator import TicketGenerator

print("[~] Load Configuration...")

AMF.SessionId = SessionID.GetSessionId()
AMF.GetEndpointForServer("FR")
loginResps = {}
sessionthread=myThread(1, "SessionUpdater", 1)
sessionthread.start()
sessionthreadlogin = myThread1(2, "TicketUpdater", 2)
sessionthreadlogin.start()

bot = commands.Bot(command_prefix="> ", description = "MovieStarPlanet Bot", intents= discord.Intents.all())

print("[#] Success to load configuration")

@bot.event
async def on_ready():
    print("reading")
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")


@bot.tree.command(name="stats", description="get information of an player with username")
@app_commands.describe(username = "enter username of the player")
@app_commands.describe(server='the server on which player is')
@app_commands.choices(server=[
    discord.app_commands.Choice(
		name="Germany",
		value="DE"
	),
	discord.app_commands.Choice(
		name="UnitedStates",
		value="US"
	),
    discord.app_commands.Choice(
		name="Denmark",
		value="DK"
	),
    discord.app_commands.Choice(
	    name="Norway",
		value="NO"
    ),
    discord.app_commands.Choice(
		name="Sweden",
		value="SE"
	),
    discord.app_commands.Choice(
		name="Finland",
		value="FI"
	),
    discord.app_commands.Choice(
		name="Netherlands",
		value="NL"
	),
    discord.app_commands.Choice(
		name="UnitedKingdom",
		value="GB"
	),
    discord.app_commands.Choice(
		name="Poland",
		value="PL"
	),
    discord.app_commands.Choice(
		name="France",
		value="FR"
	),
    discord.app_commands.Choice(
		name="Turkey",
		value="TR"
	),
    discord.app_commands.Choice(
		name="Australia",
		value="AU"
	),
    discord.app_commands.Choice(
		name="Canada",
		value="CA"
	),
    discord.app_commands.Choice(
		name="Ireland",
		value="IE"
	),
    discord.app_commands.Choice(
		name="NewZealand",
		value="NZ"
	),
    discord.app_commands.Choice(
		name="Spain",
		value="ES"
	),
])
async def stats(interaction: discord.Interaction, username: str, server: discord.app_commands.Choice[str]):
	await interaction.response.send_message("Searching **" + username + "** on **" + server.name + "**...")
	AMF.GetEndpointForServer(server.value)
	aidresp = AMF.SendAMF("MovieStarPlanet.WebService.UserSession.AMFUserSessionService.GetActorIdFromName", [ str(username) ], False)
	resp_msg = remoting.decode(aidresp)
	aid = int(str(resp_msg.bodies[0][1]).replace("<Response status=/onResult>", "").replace("</Response>", ""))
	if aid < 0:
		await interaction.edit_original_response("The user **" + username + "doesn't exist!")
	else:
		ticck = TicketGenerator.headerTicket(str((myThread1.loginResps[server.value])["loginStatus"]["ticket"]))
		loadlistresp = AMF.SendAMF("MovieStarPlanet.WebService.MovieStar.AMFMovieStarService.LoadMovieStarListRevised", [ { "Ticket": ticck, "anyAttribute": None}, [aid]], ChecksumReq=[[aid]], Ticket=ticck)
		loadlistresp = AMF.SendAMF("MovieStarPlanet.WebService.MovieStar.AMFMovieStarService.LoadMovieStarListRevised", [ { "Ticket": ticck, "anyAttribute": None}, [aid]], ChecksumReq=[[aid]], Ticket=ticck)
		embed = discord.Embed(title= str(loadlistresp[0]["Name"]) +"'s Informations", color=0xC869E5, description="<:cccc:1023261717263826965>・[Profile Id](https://syndi.lol): **" + str(loadlistresp[0]["NebulaProfileId"]) + "**\n:id:・[ActorId:](https://syndi.lol) **" + str(loadlistresp[0]["ActorId"]) + "**\n\n<:cccc:1023261544299122698>・[StarCoins:](https://syndi.lol) **" + "{:,}".format(float((loadlistresp[0]["Money"]))).replace(".0", "") + "**\n<:cccc:1023263737324515438>・[Fortune:](https://syndi.lol) **" + "{:,}".format(float(loadlistresp[0]["Fortune"])).replace(".0", "") + "**\n<:cccc:1023261775535276102>・[Fame:](https://syndi.lol) **" + "{:,}".format(float(loadlistresp[0]["Fame"])).replace(".0", "") + "**\n<:cccc:1023261608153198656>・[Level:](https://syndi.lol) **" + str(loadlistresp[0]["Level"]) + "**\n<:cccc:1023264505846841387>・[Diamonds:](https://syndi.lol) **" + "{:,}".format(float(loadlistresp[0]["Diamonds"])).replace(".0", "") + "**\n\n<:cccc:1023265039056121968>・[EyeShadow Id:](https://syndi.lol) **" + str(loadlistresp[0]["EyeShadowId"]) + "**\n<:cccc:1023261662112907305>・[EyeShadow Colors:](https://syndi.lol) **" + str(loadlistresp[0]["EyeShadowColors"]) + "**\n<:cccc:1023261825808212028>・[Eye Id:](https://syndi.lol) **" + str(loadlistresp[0]["EyeId"]) + "**\n<:cccc:1023261662112907305>・[Eye Colors:](https://syndi.lol) **" + str(loadlistresp[0]["EyeColors"]) + "**\n:nose:・[Nose Id:](https://syndi.lol) **" + str(loadlistresp[0]["NoseId"]) + "**\n[:lips:・Mouth Id:](https://syndi.lol) **" + str(loadlistresp[0]["MouthId"])+ "**\n<:cccc:1023261662112907305>・[Mouth Colors:](https://syndi.lol) **" + str(loadlistresp[0]["MouthColors"]) + "**\n<:cccc:1023266526435999794>・[Skin Color:](https://syndi.lol) **" + str(loadlistresp[0]["SkinColor"]) + "**\n\n<:cccc:1023267410087788656>・[Friends:](https://syndi.lol) **" + "{:,}".format(float(loadlistresp[0]["FriendCount"])).replace(".0", "") + "**\n<:cccc:1023268142732029982>・[VIP Friends:](https://syndi.lol) **" + "{:,}".format(float(loadlistresp[0]["FriendCountVIP"])).replace(".0", "") + "**\n<:cccc:1023268557007638619>・[VIP Days:](https://syndi.lol) **" + "{:,}".format(float(loadlistresp[0]["TotalVipDays"])).replace(".0", "") + "**\n:alarm_clock:・[Last Login:](https://syndi.lol) **" + str(datetime(int(str(loadlistresp[0]["LastLogin"]).split(",")[0]), int(str(loadlistresp[0]["LastLogin"]).split(",")[1]), int(str(loadlistresp[0]["LastLogin"]).split(",")[2]), int(str(loadlistresp[0]["LastLogin"]).split(",")[3]), int(str(loadlistresp[0]["LastLogin"]).split(",")[4]), int(str(loadlistresp[0]["LastLogin"]).split(",")[5]))) + "**")
		embed.set_thumbnail(url="https://snapshots.mspcdns.com/v1/MSP/" + server.value + "/snapshot/movieStar/" + str(loadlistresp[0]["ActorId"]) + ".jpg")
		embed2 = discord.Embed(color=0xC869E5)
		embed2.set_image(url="https://snapshots.mspcdns.com/v1/MSP/" + server.value + "/snapshot/fullsizemovieStar/" + str(loadlistresp[0]["ActorId"]) + ".jpg")
		await interaction.edit_original_response(content="", embeds=[embed, embed2])
@bot.tree.command(name="clothes", description="get information of an player with username")
@app_commands.describe(clothes_id = "enter clothes id of the clothes")
async def stats(interaction: discord.Interaction, clothes_id: int):
	AMF.GetEndpointForServer("FR")
	try:	
		loadclotheresp = AMF.SendAMF("MovieStarPlanet.WebService.MovieStar.AMFMovieStarService.LoadClothesByIds", [[clothes_id]])
		isRare = "No"
		if int(loadclotheresp[0]["ShopId"]) == -100:
			isRare = "Yes"
		isVip = "No"
		if loadclotheresp[0]["Vip"] is not None:
			if int(loadclotheresp[0]["Vip"]) > 0:
				isVip="Yes"
		embed = discord.Embed(title="Clothes Information")
		embed.add_field(name="Clothes Id:", value=str(clothes_id), inline=False)
		embed.add_field(name="Name:", value=str(loadclotheresp[0]["Name"]), inline=False)
		embed.add_field(name="SWF:", value="[" + str(loadclotheresp[0]["SWF"]) + "](https://content.mspcdns.com/swf/Shirt/" +str(loadclotheresp[0]["SWF"])+ ".swf?v=1601468245933&SMode=pqh1&MC)", inline=False)
		embed.add_field(name="Price:", value="{:,}".format(float((loadclotheresp[0]["Price"]))).replace(".0", ""), inline=False)
		embed.add_field(name= "IsRare:", value=isRare, inline=False)
		embed.add_field(name="IsVip:", value=isVip, inline=False)
		embed.add_field(name="DiamondsPrice:", value="{:,}".format(float((loadclotheresp[0]["DiamondsPrice"]))).replace(".0", ""), inline=False)
		await interaction.response.send_message(embed=embed)
	except:
		await interaction.response.send_message("Error when loading of the clothes !", ephemeral=True)
		
bot.run("OTg1MTQ1NjcyNjkwOTg3MDA4.G4lZQr.OIqxb6rNI5hnAyEHteZpbgQdrYcmhE897jSUpo")