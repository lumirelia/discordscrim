import discord
from discord import app_commands
from discord.ext import commands
import json
import os
from dotenv import load_dotenv
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.messages=True
bot = commands.Bot(command_prefix="scriminfo", intents=intents, caseinsensitive=True)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print("Commands loading...")
    await bot.tree.sync()
    print("Commands are ready.")

@bot.tree.command(name="loadherolist", description="ONLY RUN ONCE. load hero database")
async def loadherolist(interaction:discord.Interaction):
    with open('scriminfo.json', 'r+') as file:
          agudoinfo=json.load(file)
          agudoinfo['agudowins']=0
          agudoinfo['agudolosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(agudoinfo, file)   
    with open('scriminfo.json', 'r+') as file:
          alessioinfo=json.load(file)
          alessioinfo['alessiowins']=0
          alessioinfo['alessiolosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(alessioinfo, file)    
    with open('scriminfo.json', 'r+') as file:
          allaininfo=json.load(file)
          allaininfo['allainwins']=0
          allaininfo['allainlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(allaininfo, file)
    with open('scriminfo.json', 'r+') as file:
          angelainfo=json.load(file)
          angelainfo['angelawins']=0
          angelainfo['angelalosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(angelainfo, file)    
    with open('scriminfo.json', 'r+') as file:
          arkeinfo=json.load(file)
          arkeinfo['arkewins']=0
          arkeinfo['arkelosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(arkeinfo, file)    
    with open('scriminfo.json', 'r+') as file:
          arliinfo=json.load(file)
          arliinfo['arliwins']=0
          arliinfo['arlilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(arliinfo, file)
    with open('scriminfo.json', 'r+') as file:
          arthurinfo=json.load(file)
          arthurinfo['arthurwins']=0
          arthurinfo['arthurlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(arthurinfo, file)
    with open('scriminfo.json', 'r+') as file:
          atainfo=json.load(file)
          atainfo['atawins']=0
          atainfo['atalosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(atainfo, file)
    with open('scriminfo.json', 'r+') as file:
          athenainfo=json.load(file)
          athenainfo['athenawins']=0
          athenainfo['athenalosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(athenainfo, file)
    with open('scriminfo.json', 'r+') as file:
          augraninfo=json.load(file)
          augraninfo['augranwins']=0
          augraninfo['augranlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(augraninfo, file)
    with open('scriminfo.json', 'r+') as file:
          bironinfo=json.load(file)
          bironinfo['bironwins']=0
          bironinfo['bironlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(bironinfo, file) 
    with open('scriminfo.json', 'r+') as file:
          butterflyinfo=json.load(file)
          butterflyinfo['butterflywins']=0
          butterflyinfo['butterflylosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(butterflyinfo, file)
    with open('scriminfo.json', 'r+') as file:
          caiyaninfo=json.load(file)
          caiyaninfo['caiyanwins']=0
          caiyaninfo['caiyanlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(caiyaninfo, file)
    with open('scriminfo.json', 'r+') as file:
          charlotteinfo=json.load(file)
          charlotteinfo['charlottewins']=0
          charlotteinfo['charlottelosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(charlotteinfo, file)
    with open('scriminfo.json', 'r+') as file:
          cirrusinfo=json.load(file)
          cirrusinfo['cirruswins']=0
          cirrusinfo['cirruslosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(cirrusinfo, file)
    with open('scriminfo.json', 'r+') as file:
          consortyuinfo=json.load(file)
          consortyuinfo['consortyuwins']=0
          consortyuinfo['consortyulosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(consortyuinfo, file)
    with open('scriminfo.json', 'r+') as file:
          daqiaoinfo=json.load(file)
          daqiaoinfo['daqiaowins']=0
          daqiaoinfo['daqiaolosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(daqiaoinfo, file)
    with open('scriminfo.json', 'r+') as file:
          dharmainfo=json.load(file)
          dharmainfo['dharmawins']=0
          dharmainfo['dharmalosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(dharmainfo, file)
    with open('scriminfo.json', 'r+') as file:
          direnjieinfo=json.load(file)
          direnjieinfo['direnjiewins']=0
          direnjieinfo['direnjielosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(direnjieinfo, file)
    with open('scriminfo.json', 'r+') as file:
          dianweiinfo=json.load(file)
          dianweiinfo['dianweiwins']=0
          dianweiinfo['dianweilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(dianweiinfo, file)
    with open('scriminfo.json', 'r+') as file:
          diaochaninfo=json.load(file)
          diaochaninfo['diaochanwins']=0
          diaochaninfo['diaochanlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(diaochaninfo, file)
    with open('scriminfo.json', 'r+') as file:
          doliainfo=json.load(file)
          doliainfo['doliawins']=0
          doliainfo['dolialosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(doliainfo, file)
    with open('scriminfo.json', 'r+') as file:
          donghuanginfo=json.load(file)
          donghuanginfo['donghuangwins']=0
          donghuanginfo['donghuanglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(donghuanginfo, file)
    with open('scriminfo.json', 'r+') as file:
          drbianinfo=json.load(file)
          drbianinfo['drbianwins']=0
          drbianinfo['drbianlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(drbianinfo, file)
    with open('scriminfo.json', 'r+') as file:
          duninfo=json.load(file)
          duninfo['dunwins']=0
          duninfo['dunlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(duninfo, file)
    with open('scriminfo.json', 'r+') as file:
          dyadiainfo=json.load(file)
          dyadiainfo['dyadiawins']=0
          dyadiainfo['dyadialosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(dyadiainfo, file) 
    with open('scriminfo.json', 'r+') as file:
          erininfo=json.load(file)
          erininfo['erinwins']=0
          erininfo['erinlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(erininfo, file)
    with open('scriminfo.json', 'r+') as file:
          fanginfo=json.load(file)
          fanginfo['fangwins']=0
          fanginfo['fanglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(fanginfo, file)
    with open('scriminfo.json', 'r+') as file:
          fuziinfo=json.load(file)
          fuziinfo['fuziwins']=0
          fuziinfo['fuzilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(fuziinfo, file)  
    with open('scriminfo.json', 'r+') as file:
          ganmoinfo=json.load(file)
          ganmoinfo['ganmowins']=0
          ganmoinfo['ganmolosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(ganmoinfo, file)
    with open('scriminfo.json', 'r+') as file:
          gaoinfo=json.load(file)
          gaoinfo['gaowins']=0
          gaoinfo['gaolosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(gaoinfo, file)
    with open('scriminfo.json', 'r+') as file:
          garoinfo=json.load(file)
          garoinfo['garowins']=0
          garoinfo['garolosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(garoinfo, file)
    with open('scriminfo.json', 'r+') as file:
          guanyuinfo=json.load(file)
          guanyuinfo['guanyuwins']=0
          guanyuinfo['guanyulosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(guanyuinfo, file)     
    with open('scriminfo.json', 'r+') as file:
          guiguziinfo=json.load(file)
          guiguziinfo['guiguziwins']=0
          guiguziinfo['guiguzilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(guiguziinfo, file)
    with open('scriminfo.json', 'r+') as file:
          hanxininfo=json.load(file)
          hanxininfo['hanxinwins']=0
          hanxininfo['hanxinlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(hanxininfo, file)
    with open('scriminfo.json', 'r+') as file:
          heinoinfo=json.load(file)
          heinoinfo['heinowins']=0
          heinoinfo['heinolosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(heinoinfo, file)
    with open('scriminfo.json', 'r+') as file:
          houyiinfo=json.load(file)
          houyiinfo['houyiwins']=0
          houyiinfo['houyilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(houyiinfo, file)
    with open('scriminfo.json', 'r+') as file:
          huangzhonginfo=json.load(file)
          huangzhonginfo['huangzhongwins']=0
          huangzhonginfo['huangzhonglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(huangzhonginfo, file)
    with open('scriminfo.json', 'r+') as file:
          jinginfo=json.load(file)
          jinginfo['jingwins']=0
          jinginfo['jinglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(jinginfo, file) 
    with open('scriminfo.json', 'r+') as file:
          kaizerinfo=json.load(file)
          kaizerinfo['kaizerwins']=0
          kaizerinfo['kaizerlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(kaizerinfo, file)    
    with open('scriminfo.json', 'r+') as file:
          kuiinfo=json.load(file)
          kuiinfo['kuiwins']=0
          kuiinfo['kuilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(kuiinfo, file)
    with open('scriminfo.json', 'r+') as file:
          kongminginfo=json.load(file)
          kongminginfo['kongmingwins']=0
          kongminginfo['kongminglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(kongminginfo, file)
    with open('scriminfo.json', 'r+') as file:
          ladysuninfo=json.load(file)
          ladysuninfo['ladysunwins']=0
          ladysuninfo['ladysunlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(ladysuninfo, file) 
    with open('scriminfo.json', 'r+') as file:
          ladyzheninfo=json.load(file)
          ladyzheninfo['ladyzhenwins']=0
          ladyzheninfo['ladyzhenlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(ladyzheninfo, file)
    with open('scriminfo.json', 'r+') as file:
          laminfo=json.load(file)
          laminfo['lamwins']=0
          laminfo['lamlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(laminfo, file)
    with open('scriminfo.json', 'r+') as file:
          libaiinfo=json.load(file)
          libaiinfo['libaiwins']=0
          libaiinfo['libailosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(libaiinfo, file)
    with open('scriminfo.json', 'r+') as file:
          lixininfo=json.load(file)
          lixininfo['lixinwins']=0
          lixininfo['lixinlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(lixininfo, file)
    with open('scriminfo.json', 'r+') as file:
          lianpoinfo=json.load(file)
          lianpoinfo['lianpowins']=0
          lianpoinfo['lianpolosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(lianpoinfo, file)
    with open('scriminfo.json', 'r+') as file:
          lianginfo=json.load(file)
          lianginfo['liangwins']=0
          lianginfo['lianglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(lianginfo, file) 
    with open('scriminfo.json', 'r+') as file:
          liubanginfo=json.load(file)
          liubanginfo['liubangwins']=0
          liubanginfo['liubanglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(liubanginfo, file)
    with open('scriminfo.json', 'r+') as file:
          liubeiinfo=json.load(file)
          liubeiinfo['liubeiwins']=0
          liubeiinfo['liubeilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(liubeiinfo, file)
    with open('scriminfo.json', 'r+') as file:
          liushaninfo=json.load(file)
          liushaninfo['liushanwins']=0
          liushaninfo['liushanlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(liushaninfo, file)
    with open('scriminfo.json', 'r+') as file:
          loonginfo=json.load(file)
          loonginfo['loongwins']=0
          loonginfo['loonglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(loonginfo, file)
    with open('scriminfo.json', 'r+') as file:
          lubuinfo=json.load(file)
          lubuinfo['lubuwins']=0
          lubuinfo['lubulosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(lubuinfo, file)
    with open('scriminfo.json', 'r+') as file:
          luarainfo=json.load(file)
          luarainfo['luarawins']=0
          luarainfo['luaralosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(luarainfo, file)
    with open('scriminfo.json', 'r+') as file:
          lubaninfo=json.load(file)
          lubaninfo['lubanwins']=0
          lubaninfo['lubanlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(lubaninfo, file)
    with open('scriminfo.json', 'r+') as file:
          lunainfo=json.load(file)
          lunainfo['lunawins']=0
          lunainfo['lunalosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(lunainfo, file)
    with open('scriminfo.json', 'r+') as file:
          maiinfo=json.load(file)
          maiinfo['maiwins']=0
          maiinfo['mailosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(maiinfo, file)
    with open('scriminfo.json', 'r+') as file:
          marcoinfo=json.load(file)
          marcoinfo['marcowins']=0
          marcoinfo['marcolosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(marcoinfo, file)
    with open('scriminfo.json', 'r+') as file:
          mayeneinfo=json.load(file)
          mayeneinfo['mayenewins']=0
          mayeneinfo['mayenelosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(mayeneinfo, file) 
    with open('scriminfo.json', 'r+') as file:
          mengyainfo=json.load(file)
          mengyainfo['mengyawins']=0
          mengyainfo['mengyalosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(mengyainfo, file)
    with open('scriminfo.json', 'r+') as file:
          menkiinfo=json.load(file)
          menkiinfo['menkiwins']=0
          menkiinfo['menkilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(menkiinfo, file)
    with open('scriminfo.json', 'r+') as file:
          miyueinfo=json.load(file)
          miyueinfo['miyuewins']=0
          miyueinfo['miyuelosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(miyueinfo, file)
    with open('scriminfo.json', 'r+') as file:
          miladyinfo=json.load(file)
          miladyinfo['miladywins']=0
          miladyinfo['miladylosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(miladyinfo, file)  
    with open('scriminfo.json', 'r+') as file:
          minginfo=json.load(file)
          minginfo['mingwins']=0
          minginfo['minglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(minginfo, file)
    with open('scriminfo.json', 'r+') as file:
          moziinfo=json.load(file)
          moziinfo['moziwins']=0
          moziinfo['mozilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(moziinfo, file)
    with open('scriminfo.json', 'r+') as file:
          mulaninfo=json.load(file)
          mulaninfo['mulanwins']=0
          mulaninfo['mulanlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(mulaninfo, file)
    with open('scriminfo.json', 'r+') as file:
          musashiinfo=json.load(file)
          musashiinfo['musashiwins']=0
          musashiinfo['musashilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(musashiinfo, file)
    with open('scriminfo.json', 'r+') as file:
          nakoruruinfo=json.load(file)
          nakoruruinfo['nakoruruwins']=0
          nakoruruinfo['nakorurulosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(nakoruruinfo, file)
    with open('scriminfo.json', 'r+') as file:
          nezhainfo=json.load(file)
          nezhainfo['nezhawins']=0
          nezhainfo['nezhalosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(nezhainfo, file)
    with open('scriminfo.json', 'r+') as file:
          nuwainfo=json.load(file)
          nuwainfo['nuwawins']=0
          nuwainfo['nuwalosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(nuwainfo, file)
    with open('scriminfo.json', 'r+') as file:
          peiinfo=json.load(file)
          peiinfo['peiwins']=0
          peiinfo['peilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(peiinfo, file)
    with open('scriminfo.json', 'r+') as file:
          lanlinginfo=json.load(file)
          lanlinginfo['lanlingwins']=0
          lanlinginfo['lanlinglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(lanlinginfo, file)
    with open('scriminfo.json', 'r+') as file:
          frostinfo=json.load(file)
          frostinfo['frostwins']=0
          frostinfo['frostlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(frostinfo, file)
    with open('scriminfo.json', 'r+') as file:
          sakeerinfo=json.load(file)
          sakeerinfo['sakeerwins']=0
          sakeerinfo['sakeerlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(sakeerinfo, file)
    with open('scriminfo.json', 'r+') as file:
          shangguaninfo=json.load(file)
          shangguaninfo['shangguanwins']=0
          shangguaninfo['shangguanlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(shangguaninfo, file)
    with open('scriminfo.json', 'r+') as file:
          shiinfo=json.load(file)
          shiinfo['shiwins']=0
          shiinfo['shilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(shiinfo, file)
    with open('scriminfo.json', 'r+') as file:
          shouyueinfo=json.load(file)
          shouyueinfo['shouyuewins']=0
          shouyueinfo['shouyuelosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(shouyueinfo, file)
    with open('scriminfo.json', 'r+') as file:
          simayiinfo=json.load(file)
          simayiinfo['simayiwins']=0
          simayiinfo['simayilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(simayiinfo, file)
    with open('scriminfo.json', 'r+') as file:
          sunbininfo=json.load(file)
          sunbininfo['sunbinwins']=0
          sunbininfo['sunbinlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(sunbininfo, file)
    with open('scriminfo.json', 'r+') as file:
          sunceinfo=json.load(file)
          sunceinfo['suncewins']=0
          sunceinfo['suncelosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(sunceinfo, file)
    with open('scriminfo.json', 'r+') as file:
          ukyoinfo=json.load(file)
          ukyoinfo['ukyowins']=0
          ukyoinfo['ukyolosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(ukyoinfo, file)
    with open('scriminfo.json', 'r+') as file:
          wukonginfo=json.load(file)
          wukonginfo['wukongwins']=0
          wukonginfo['wukonglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(wukonginfo, file)
    with open('scriminfo.json', 'r+') as file:
          xiangyuinfo=json.load(file)
          xiangyuinfo['xiangyuwins']=0
          xiangyuinfo['xiangyulosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(xiangyuinfo, file)
    with open('scriminfo.json', 'r+') as file:
          xiaoqiaoinfo=json.load(file)
          xiaoqiaoinfo['xiaoqiaowins']=0
          xiaoqiaoinfo['xiaoqiaolosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(xiaoqiaoinfo, file)
    with open('scriminfo.json', 'r+') as file:
          xuanceinfo=json.load(file)
          xuanceinfo['xuancewins']=0
          xuanceinfo['xuancelosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(xuanceinfo, file)
    with open('scriminfo.json', 'r+') as file:
          yangjianinfo=json.load(file)
          yangjianinfo['yangjianwins']=0
          yangjianinfo['yangjianlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(yangjianinfo, file)
    with open('scriminfo.json', 'r+') as file:
          yaoinfo=json.load(file)
          yaoinfo['yaowins']=0
          yaoinfo['yaolosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(yaoinfo, file)
    with open('scriminfo.json', 'r+') as file:
          yariainfo=json.load(file)
          yariainfo['yariawins']=0
          yariainfo['yarialosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(yariainfo, file) 
    with open('scriminfo.json', 'r+') as file:
          yinginfo=json.load(file)
          yinginfo['yingwins']=0
          yinginfo['yinglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(yinginfo, file)
    with open('scriminfo.json', 'r+') as file:
          yixinginfo=json.load(file)
          yixinginfo['yixingwins']=0
          yixinginfo['yixinglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(yixinginfo, file)
    with open('scriminfo.json', 'r+') as file:
          yuhuaninfo=json.load(file)
          yuhuaninfo['yuhuanwins']=0
          yuhuaninfo['yuhuanlosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(yuhuaninfo, file)
    with open('scriminfo.json', 'r+') as file:
          zhangfeiinfo=json.load(file)
          zhangfeiinfo['zhangfeiwins']=0
          zhangfeiinfo['zhangfeilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(zhangfeiinfo, file)
    with open('scriminfo.json', 'r+') as file:
          zhouyuinfo=json.load(file)
          zhouyuinfo['zhouyuwins']=0
          zhouyuinfo['zhouyulosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(zhouyuinfo, file)
    with open('scriminfo.json', 'r+') as file:
          zhuangziinfo=json.load(file)
          zhuangziinfo['zhuangziwins']=0
          zhuangziinfo['zhuangzilosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(zhuangziinfo, file)
    with open('scriminfo.json', 'r+') as file:
          zilonginfo=json.load(file)
          zilonginfo['zilongwins']=0
          zilonginfo['zilonglosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(zilonginfo, file)
    with open('scriminfo.json', 'r+') as file:
          ziyainfo=json.load(file)
          ziyainfo['ziyawins']=0
          ziyainfo['ziyalosses']=0
    with open('scriminfo.json', 'w') as file:
        json.dump(ziyainfo, file)
    await interaction.response.send_message("heroes loaded. can now use /scriminfo")

@bot.tree.command(name="scriminfo", description="modify scrim info")
async def scriminfo(interaction:discord.Interaction, hero:str, result:str):
    if hero =="agudo":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["agudowins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("agudo wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["agudolosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("agudo losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="alessio":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["alessiowins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("alessio wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["alessiolosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("alessio losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="allain":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["allainwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("allain wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["allainlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("allain losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="angela":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["angelawins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("angela wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["angelalosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("angela losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="arli":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["arliwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("arli wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["arlilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("arli losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")

    if hero =="arthur":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["arthurwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("arthur wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["arthurlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("arthur losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")

    if hero =="ata":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["atawins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("ata wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["atalosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("ata losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="athena":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["athenawins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("athena wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["athenalosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("athena losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="augran":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["augranwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("augran wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["augranlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("augran losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="biron":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["bironwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("biron wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["bironlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("biron losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="butterfly":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["butterflywins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("butterfly wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["butterflylosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("butterfly losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="caiyan":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["caiyanwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("caiyan wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["caiyanlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("caiyan losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="charlotte":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["charlottewins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("charlotte wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["charlottelosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("charlotte losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="cirrus":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["cirruswins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("cirrus wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["cirruslosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("cirrus losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="consortyu":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["consortyuwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("consortyu wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["consortyulosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("consortyu losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="daqiao":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["daqiaowins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("daqiao wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["daqiaolosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("daqiao losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="daji":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["dajiwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("daji wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["dajilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("daji losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="dharma":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["dharmawins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("dharma wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["dharmalosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("dharma losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="direnjie":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["direnjiewins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("direnjie wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["direnjielosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("direnjie losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="dianwei":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["dianweiwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("dianwei wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["dianweilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("dianwei losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="diaochan":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["diaochanwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("diaochan wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["diaochanlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("diaochan losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="dolia":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["doliawins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("dolia wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["dolialosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("dolia losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="donghuang":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["donghuangwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("donghuang wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["donghuanglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("donghuang losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="drbian":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["drbianwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("drbian wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["drbianlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("drbian losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="dun":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["dunwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("dun wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["dunlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("dun losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="dyadia":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["dyadiawins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("dyadia wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["dyadialosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("dyadia losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="erin":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["erinwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("erin wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["erinlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("erin losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="fang":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["fangwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("fang wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["fanglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("fang losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="fuzi":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["fuziwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("fuzi wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["fuzilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("fuzi losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="ganmo":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["ganmowins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("ganmo wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["ganmolosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("ganmo losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="garo":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["garowins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("garo wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["garolosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("garo losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="guanyu":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["guanyuwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("guanyu wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["guanyulosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("guanyu losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="guiguzi":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["guiguziwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("guiguzi wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["guiguzilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("guiguzi losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="hanxin":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["hanxinwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("hanxin wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["hanxinlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("hanxin losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="heino":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["heinowins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("heino wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["heinolosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("heino losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="houyi":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["houyiwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("houyi wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["houyilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("houyi losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="huangzhong":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["huangzhongwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("huangzhong wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["huangzhonglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("huangzhong losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="jing":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["jingwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("jing wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["jinglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("jing losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="kaizer":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["kaizerwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("kaizer wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["kaizerlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("kaizer losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="kongming":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["kongmingwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("kongming wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["kongminglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("kongming losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="kui":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["kuiwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("kui wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["kuilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("kui losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="ladysun":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["ladysunwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("ladysun wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["ladysunlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("ladysun losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="ladyzhen":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["ladyzhenwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("ladyzhen wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["ladyzhenlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("ladyzhen losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="lam":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lamwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("lam wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lamlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("lam losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="libai":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["libaiwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("libai wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["libailosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("libai losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="lixin":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lixinwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("lixin wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lixinlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("lixin losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="lianpo":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lianpowins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("lianpo wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lianpolosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("lianpo losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="liang":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["liangwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("liang wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lianglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("liang losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="liubang":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["liubangwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("liubang wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["liubanglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("liubang losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="liubei":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["liubeiwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("liubei wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["liubeilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("liubei losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="liushan":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["liushanwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("liushan wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["liushanlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("liushan losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="loong":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["loongwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("loong wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["loonglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("loong losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="lubu":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lubuwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("lubu wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lubulosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("lubu losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="luara":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["luarawins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("luara wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["luaralosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("luara losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="luban":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lubanwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("luban wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lubanlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("luban losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="luna":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lunawins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("luna wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lunalosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("luna losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="mai":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["maiwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("mai wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["mailosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("mai losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="marco":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["marcowins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("marco wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["marcolosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("marco losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="mayene":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["mayenewins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("mayene wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["mayenelosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("mayene losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="mengya":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["mengyawins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("mengya wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["mengyalosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("mengya losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="menki":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["menkiwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("menki wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["menkilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("menki losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="miyue":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["miyuewins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("miyue wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["miyuelosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("miyue losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="milady":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["miladywins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("milady wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["miladylosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("milady losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="ming":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["mingwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("ming wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["minglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("ming losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="mozi":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["moziwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("mozi wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["mozilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("mozi losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="mulan":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["mulanwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("mulan wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["mulanlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("mulan losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="musashi":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["musashiwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("musashi wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["musashilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("musashi losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="nakoruru":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["nakoruruwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("nakoruru wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["nakorurulosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("nakoruru losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="nezha":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["nezhawins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("nezha wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["nezhalosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("nezha losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="nuwa":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["nuwawins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("nuwa wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["nuwalosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("nuwa losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="pei":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["peiwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("pei wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["peilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("pei losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="lanling":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lanlingwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("lanling wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["lanlinglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("lanling losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="frost":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["frostwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("frost wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["frostlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("frost losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="sakeer":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["sakeerwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("sakeer wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["sakeerlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("sakeer losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="shangguan":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["shangguanwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("shangguan wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["shangguanlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("shangguan losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="shi":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["shiwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("shi wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["shilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("shi losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="shouyue":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["shouyuewins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("shouyue wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["shouyuelosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("shouyue losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="simayi":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["simayiwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("simayi wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["simayilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("simayi losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="sunbin":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["sunbinwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("sunbin wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["sunbinlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("sunbin losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="sunce":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["suncewins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("sunce wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["suncelosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("sunce losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="ukyo":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["ukyowins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("ukyo wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["ukyolosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("ukyo losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="wukong":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["wukongwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("wukong wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["wukonglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("wukong losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="wuyan":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["wuyanwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("wuyan wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["wuyanlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("wuyan losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="xiangyu":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["xiangyuwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("xiangyu wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["xiangyulosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("xiangyu losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="xiaoqiao":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["xiaoqiaowins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("xiaoqiao wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["xiaoqiaolosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("xiaoqiao losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="xuance":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["xuancewins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("xuance wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["xuancelosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("xuance losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="yangjian":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["yangjianwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("yangjian wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["yangjianlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("yangjian losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="yao":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["yaowins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("yao wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["yaolosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("yao losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="yaria":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["yariawins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("yaria wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["yarialosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("yaria losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="ying":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["yingwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("ying wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["yinglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("ying losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="yixing":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["yixingwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("yixing wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["yixinglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("yixing losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="yuhuan":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["yuhuanwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("yuhuan wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["yuhuanlosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("yuhuan losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="zhangfei":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["zhangfeiwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("zhangfei wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["zhangfeilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("zhangfei losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="zhouyu":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["zhouyuwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("zhouyu wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["zhouyulosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("zhouyu losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="zhuangzi":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["zhuangziwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("zhuangzi wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["zhuangzilosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("zhuangzi losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="zilong":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["zilongwins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("zilong wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["zilonglosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("zilong losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    if hero =="ziya":
        if result=="win":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["ziyawins"] +=1
             json.dump(data, file)   
             await interaction.response.send_message("ziya wins modified. check hero info with /database")
        elif result=="loss":
            with open('scriminfo.json', 'r+') as file:
             data=json.load(file)
            with open('scriminfo.json', 'r+') as file:
             data["ziyalosses"] +=1
             json.dump(data, file)  
             await interaction.response.send_message("ziya losses modified. check hero info with /database")
        else:
           await interaction.response.send_message("error. please only input win or loss for result. thank you")
    else:
       await interaction.response.send_message("please input valid hero.")

@bot.tree.command(name="database", description="view scrim info")
async def database(interaction: discord.Interaction, hero:str):
    if hero == "agudo":
        with open('scriminfo.json', 'r') as file:
            agudo=json.load(file)
            agudowins=agudo["agudowins"]
            agudolosses=agudo["agudolosses"]
            agudomessage= "Wins: {}, Losses: {}" .format(agudowins, agudolosses)
        await interaction.response.send_message(agudomessage)
    elif hero == "alessio":
        with open('scriminfo.json', 'r') as file:
            alessio=json.load(file)
            alessiowins=alessio["alessiowins"]
            alessiolosses=alessio["alessiolosses"]
            alessiomessage= "Wins: {}, Losses: {}" .format(alessiowins, alessiolosses)
        await interaction.response.send_message(alessiomessage)
    elif hero == "allain":
        with open('scriminfo.json', 'r') as file:
            allain=json.load(file)
            allainwins=allain["allainwins"]
            allainlosses=allain["allainlosses"]
            allainmessage= "Wins: {}, Losses: {}" .format(allainwins, allainlosses)
        await interaction.response.send_message(allainmessage)
    elif hero == "angela":
        with open('scriminfo.json', 'r') as file:
            angela=json.load(file)
            angelawins=angela["angelawins"]
            angelalosses=angela["angelalosses"]
            angelamessage= "Wins: {}, Losses: {}" .format(angelawins, angelalosses)
        await interaction.response.send_message(angelamessage)
    elif hero == "arke":
        with open('scriminfo.json', 'r') as file:
            arke=json.load(file)
            arkewins=arke["arkewins"]
            arkelosses=arke["arkelosses"]
            arkemessage= "Wins: {}, Losses: {}" .format(arkewins, arkelosses)
        await interaction.response.send_message(arkemessage)
    elif hero == "arli":
        with open('scriminfo.json', 'r') as file:
            arli=json.load(file)
            arliwins=arli["arliwins"]
            arlilosses=arli["arlilosses"]
            arlimessage= "Wins: {}, Losses: {}" .format(arliwins, arlilosses)
        await interaction.response.send_message(arlimessage)
    elif hero == "arthur":
        with open('scriminfo.json', 'r') as file:
            arthur=json.load(file)
            arthurwins=arthur["arthurwins"]
            arthurlosses=arthur["arthurlosses"]
            arthurmessage= "Wins: {}, Losses: {}" .format(arthurwins, arthurlosses)
        await interaction.response.send_message(arthurmessage)
    elif hero == "ata":
        with open('scriminfo.json', 'r') as file:
            ata=json.load(file)
            atawins=ata["atawins"]
            atalosses=ata["atalosses"]
            atamessage= "Wins: {}, Losses: {}" .format(atawins, atalosses)
        await interaction.response.send_message(atamessage)
    elif hero == "athena":
        with open('scriminfo.json', 'r') as file:
            athena=json.load(file)
            athenawins=athena["athenawins"]
            athenalosses=athena["athenalosses"]
            athenamessage= "Wins: {}, Losses: {}" .format(athenawins, athenalosses)
        await interaction.response.send_message(athenamessage)
    elif hero == "augran":
        with open('scriminfo.json', 'r') as file:
            augran=json.load(file)
            augranwins=augran["augranwins"]
            augranlosses=augran["augranlosses"]
            augranmessage= "Wins: {}, Losses: {}" .format(augranwins, augranlosses)
        await interaction.response.send_message(augranmessage)
    elif hero == "biron":
        with open('scriminfo.json', 'r') as file:
            biron=json.load(file)
            bironwins=biron["bironwins"]
            bironlosses=biron["bironlosses"]
            bironmessage= "Wins: {}, Losses: {}" .format(bironwins, bironlosses)
        await interaction.response.send_message(bironmessage)
    elif hero == "butterfly":
        with open('scriminfo.json', 'r') as file:
            butterfly=json.load(file)
            butterflywins=butterfly["butterflywins"]
            butterflylosses=butterfly["butterflylosses"]
            butterflymessage= "Wins: {}, Losses: {}" .format(butterflywins, butterflylosses)
        await interaction.response.send_message(butterflymessage)
    elif hero == "caiyan":
        with open('scriminfo.json', 'r') as file:
            caiyan=json.load(file)
            caiyanwins=caiyan["caiyanwins"]
            caiyanlosses=caiyan["caiyanlosses"]
            caiyanmessage= "Wins: {}, Losses: {}" .format(caiyanwins, caiyanlosses)
        await interaction.response.send_message(caiyanmessage)
    elif hero == "charlotte":
        with open('scriminfo.json', 'r') as file:
            charlotte=json.load(file)
            charlottewins=charlotte["charlottewins"]
            charlottelosses=charlotte["charlottelosses"]
            charlottemessage= "Wins: {}, Losses: {}" .format(charlottewins, charlottelosses)
        await interaction.response.send_message(charlottemessage)
    elif hero == "cirrus":
        with open('scriminfo.json', 'r') as file:
            cirrus=json.load(file)
            cirruswins=cirrus["cirruswins"]
            cirruslosses=cirrus["cirruslosses"]
            cirrusmessage= "Wins: {}, Losses: {}" .format(cirruswins, cirruslosses)
        await interaction.response.send_message(cirrusmessage)
    elif hero == "consortyu":
        with open('scriminfo.json', 'r') as file:
            consortyu=json.load(file)
            consortyuwins=consortyu["consortyuwins"]
            consortyulosses=consortyu["consortyulosses"]
            consortyumessage= "Wins: {}, Losses: {}" .format(consortyuwins, consortyulosses)
        await interaction.response.send_message(consortyumessage)
    elif hero == "daqiao":
        with open('scriminfo.json', 'r') as file:
            daqiao=json.load(file)
            daqiaowins=daqiao["daqiaowins"]
            daqiaolosses=daqiao["daqiaolosses"]
            daqiaomessage= "Wins: {}, Losses: {}" .format(daqiaowins, daqiaolosses)
        await interaction.response.send_message(daqiaomessage)
    elif hero == "daji":
        with open('scriminfo.json', 'r') as file:
            daji=json.load(file)
            dajiwins=daji["dajiwins"]
            dajilosses=daji["dajilosses"]
            dajimessage= "Wins: {}, Losses: {}" .format(dajiwins, dajilosses)
        await interaction.response.send_message(dajimessage)
    elif hero == "dharma":
        with open('scriminfo.json', 'r') as file:
            dharma=json.load(file)
            dharmawins=dharma["dharmawins"]
            dharmalosses=dharma["dharmalosses"]
            dharmamessage= "Wins: {}, Losses: {}" .format(dharmawins, dharmalosses)
        await interaction.response.send_message(dharmamessage)
    elif hero == "direnjie":
        with open('scriminfo.json', 'r') as file:
            direnjie=json.load(file)
            direnjiewins=direnjie["direnjiewins"]
            direnjielosses=direnjie["direnjielosses"]
            direnjiemessage= "Wins: {}, Losses: {}" .format(direnjiewins, direnjielosses)
        await interaction.response.send_message(direnjiemessage)
    elif hero == "dianwei":
        with open('scriminfo.json', 'r') as file:
            dianwei=json.load(file)
            dianweiwins=dianwei["dianweiwins"]
            dianweilosses=dianwei["dianweilosses"]
            dianweimessage= "Wins: {}, Losses: {}" .format(dianweiwins, dianweilosses)
        await interaction.response.send_message(dianweimessage)
    elif hero == "diaochan":
        with open('scriminfo.json', 'r') as file:
            diaochan=json.load(file)
            diaochanwins=diaochan["diaochanwins"]
            diaochanlosses=diaochan["diaochanlosses"]
            diaochanmessage= "Wins: {}, Losses: {}" .format(diaochanwins, diaochanlosses)
        await interaction.response.send_message(diaochanmessage)
    elif hero == "dolia":
        with open('scriminfo.json', 'r') as file:
            dolia=json.load(file)
            doliawins=dolia["doliawins"]
            dolialosses=dolia["dolialosses"]
            doliamessage= "Wins: {}, Losses: {}" .format(doliawins, dolialosses)
        await interaction.response.send_message(doliamessage)
    elif hero == "donghuang":
        with open('scriminfo.json', 'r') as file:
            donghuang=json.load(file)
            donghuangwins=donghuang["donghuangwins"]
            donghuanglosses=donghuang["donghuanglosses"]
            donghuangmessage= "Wins: {}, Losses: {}" .format(donghuangwins, donghuanglosses)
        await interaction.response.send_message(donghuangmessage)
    elif hero == "drbian":
        with open('scriminfo.json', 'r') as file:
            drbian=json.load(file)
            drbianwins=drbian["drbianwins"]
            drbianlosses=drbian["drbianlosses"]
            drbianmessage= "Wins: {}, Losses: {}" .format(drbianwins, drbianlosses)
        await interaction.response.send_message(drbianmessage)
    elif hero == "dun":
        with open('scriminfo.json', 'r') as file:
            dun=json.load(file)
            dunwins=dun["dunwins"]
            dunlosses=dun["dunlosses"]
            dunmessage= "Wins: {}, Losses: {}" .format(dunwins, dunlosses)
        await interaction.response.send_message(dunmessage)
    elif hero == "dyadia":
        with open('scriminfo.json', 'r') as file:
            dyadia=json.load(file)
            dyadiawins=dyadia["dyadiawins"]
            dyadialosses=dyadia["dyadialosses"]
            dyadiamessage= "Wins: {}, Losses: {}" .format(dyadiawins, dyadialosses)
        await interaction.response.send_message(dyadiamessage)
    elif hero == "erin":
        with open('scriminfo.json', 'r') as file:
            erin=json.load(file)
            erinwins=erin["erinwins"]
            erinlosses=erin["erinlosses"]
            erinmessage= "Wins: {}, Losses: {}" .format(erinwins, erinlosses)
        await interaction.response.send_message(erinmessage)
    elif hero == "fang":
        with open('scriminfo.json', 'r') as file:
            fang=json.load(file)
            fangwins=fang["fangwins"]
            fanglosses=fang["fanglosses"]
            fangmessage= "Wins: {}, Losses: {}" .format(fangwins, fanglosses)
        await interaction.response.send_message(fangmessage)
    elif hero == "fuzi":
        with open('scriminfo.json', 'r') as file:
            fuzi=json.load(file)
            fuziwins=fuzi["fuziwins"]
            fuzilosses=fuzi["fuzilosses"]
            fuzimessage= "Wins: {}, Losses: {}" .format(fuziwins, fuzilosses)
        await interaction.response.send_message(fuzimessage)
    elif hero == "ganmo":
        with open('scriminfo.json', 'r') as file:
            ganmo=json.load(file)
            ganmowins=ganmo["ganmowins"]
            ganmolosses=ganmo["ganmolosses"]
            ganmomessage= "Wins: {}, Losses: {}" .format(ganmowins, ganmolosses)
        await interaction.response.send_message(ganmomessage)
    elif hero == "gao":
        with open('scriminfo.json', 'r') as file:
            gao=json.load(file)
            gaowins=gao["gaowins"]
            gaolosses=gao["gaolosses"]
            gaomessage= "Wins: {}, Losses: {}" .format(gaowins, gaolosses)
        await interaction.response.send_message(gaomessage)
    elif hero == "garo":
        with open('scriminfo.json', 'r') as file:
            garo=json.load(file)
            garowins=garo["garowins"]
            garolosses=garo["garolosses"]
            garomessage= "Wins: {}, Losses: {}" .format(garowins, garolosses)
        await interaction.response.send_message(garomessage)
    elif hero == "guanyu":
        with open('scriminfo.json', 'r') as file:
            guanyu=json.load(file)
            guanyuwins=guanyu["guanyuwins"]
            guanyulosses=guanyu["guanyulosses"]
            guanyumessage= "Wins: {}, Losses: {}" .format(guanyuwins, guanyulosses)
        await interaction.response.send_message(guanyumessage)
    elif hero == "guiguzi":
        with open('scriminfo.json', 'r') as file:
            guiguzi=json.load(file)
            guiguziwins=guiguzi["guiguziwins"]
            guiguzilosses=guiguzi["guiguzilosses"]
            guiguzimessage= "Wins: {}, Losses: {}" .format(guiguziwins, guiguzilosses)
        await interaction.response.send_message(guiguzimessage)
    elif hero == "hanxin":
        with open('scriminfo.json', 'r') as file:
            hanxin=json.load(file)
            hanxinwins=hanxin["hanxinwins"]
            hanxinlosses=hanxin["hanxinlosses"]
            hanxinmessage= "Wins: {}, Losses: {}" .format(hanxinwins, hanxinlosses)
        await interaction.response.send_message(hanxinmessage)
    elif hero == "heino":
        with open('scriminfo.json', 'r') as file:
            heino=json.load(file)
            heinowins=heino["heinowins"]
            heinolosses=heino["heinolosses"]
            heinomessage= "Wins: {}, Losses: {}" .format(heinowins, heinolosses)
        await interaction.response.send_message(heinomessage)
    elif hero == "houyi":
        with open('scriminfo.json', 'r') as file:
            houyi=json.load(file)
            houyiwins=houyi["houyiwins"]
            houyilosses=houyi["houyilosses"]
            houyimessage= "Wins: {}, Losses: {}" .format(houyiwins, houyilosses)
        await interaction.response.send_message(houyimessage)
    elif hero == "huangzhong":
        with open('scriminfo.json', 'r') as file:
            huangzhong=json.load(file)
            huangzhongwins=huangzhong["huangzhongwins"]
            huangzhonglosses=huangzhong["huangzhonglosses"]
            huangzhongmessage= "Wins: {}, Losses: {}" .format(huangzhongwins, huangzhonglosses)
        await interaction.response.send_message(huangzhongmessage)
    elif hero == "jing":
        with open('scriminfo.json', 'r') as file:
            jing=json.load(file)
            jingwins=jing["jingwins"]
            jinglosses=jing["jinglosses"]
            jingmessage= "Wins: {}, Losses: {}" .format(jingwins, jinglosses)
        await interaction.response.send_message(jingmessage)
    elif hero == "kaizer":
        with open('scriminfo.json', 'r') as file:
            kaizer=json.load(file)
            kaizerwins=kaizer["kaizerwins"]
            kaizerlosses=kaizer["kaizerlosses"]
            kaizermessage= "Wins: {}, Losses: {}" .format(kaizerwins, kaizerlosses)
        await interaction.response.send_message(kaizermessage)
    elif hero == "kongming":
        with open('scriminfo.json', 'r') as file:
            kongming=json.load(file)
            kongmingwins=kongming["kongmingwins"]
            kongminglosses=kongming["kongminglosses"]
            kongmingmessage= "Wins: {}, Losses: {}" .format(kongmingwins, kongminglosses)
        await interaction.response.send_message(kongmingmessage)
    elif hero == "kui":
        with open('scriminfo.json', 'r') as file:
            kui=json.load(file)
            kuiwins=kui["kuiwins"]
            kuilosses=kui["kuilosses"]
            kuimessage= "Wins: {}, Losses: {}" .format(kuiwins, kuilosses)
        await interaction.response.send_message(kuimessage)
    elif hero == "ladysun":
        with open('scriminfo.json', 'r') as file:
            ladysun=json.load(file)
            ladysunwins=ladysun["ladysunwins"]
            ladysunlosses=ladysun["ladysunlosses"]
            ladysunmessage= "Wins: {}, Losses: {}" .format(ladysunwins, ladysunlosses)
        await interaction.response.send_message(ladysunmessage)
    elif hero == "ladyzhen":
        with open('scriminfo.json', 'r') as file:
            ladyzhen=json.load(file)
            ladyzhenwins=ladyzhen["ladyzhenwins"]
            ladyzhenlosses=ladyzhen["ladyzhenlosses"]
            ladyzhenmessage= "Wins: {}, Losses: {}" .format(ladyzhenwins, ladyzhenlosses)
        await interaction.response.send_message(ladyzhenmessage)
    elif hero == "lam":
        with open('scriminfo.json', 'r') as file:
            lam=json.load(file)
            lamwins=lam["lamwins"]
            lamlosses=lam["lamlosses"]
            lammessage= "Wins: {}, Losses: {}" .format(lamwins, lamlosses)
        await interaction.response.send_message(lammessage)
    elif hero == "libai":
        with open('scriminfo.json', 'r') as file:
            libai=json.load(file)
            libaiwins=libai["libaiwins"]
            libailosses=libai["libailosses"]
            libaimessage= "Wins: {}, Losses: {}" .format(libaiwins, libailosses)
        await interaction.response.send_message(libaimessage)
    elif hero == "lixin":
        with open('scriminfo.json', 'r') as file:
            lixin=json.load(file)
            lixinwins=lixin["lixinwins"]
            lixinlosses=lixin["lixinlosses"]
            lixinmessage= "Wins: {}, Losses: {}" .format(lixinwins, lixinlosses)
        await interaction.response.send_message(lixinmessage)
    elif hero == "lianpo":
        with open('scriminfo.json', 'r') as file:
            lianpo=json.load(file)
            lianpowins=lianpo["lianpowins"]
            lianpolosses=lianpo["lianpolosses"]
            lianpomessage= "Wins: {}, Losses: {}" .format(lianpowins, lianpolosses)
        await interaction.response.send_message(lianpomessage)
    elif hero == "liang":
        with open('scriminfo.json', 'r') as file:
            liang=json.load(file)
            liangwins=liang["liangwins"]
            lianglosses=liang["lianglosses"]
            liangmessage= "Wins: {}, Losses: {}" .format(liangwins, lianglosses)
        await interaction.response.send_message(liangmessage)
    elif hero == "liubang":
        with open('scriminfo.json', 'r') as file:
            liubang=json.load(file)
            liubangwins=liubang["liubangwins"]
            liubanglosses=liubang["liubanglosses"]
            liubangmessage= "Wins: {}, Losses: {}" .format(liubangwins, liubanglosses)
        await interaction.response.send_message(liubangmessage)
    elif hero == "liubei":
        with open('scriminfo.json', 'r') as file:
            liubei=json.load(file)
            liubeiwins=liubei["liubeiwins"]
            liubeilosses=liubei["liubeilosses"]
            liubeimessage= "Wins: {}, Losses: {}" .format(liubeiwins, liubeilosses)
        await interaction.response.send_message(liubeimessage)
    elif hero == "liushan":
        with open('scriminfo.json', 'r') as file:
            liushan=json.load(file)
            liushanwins=liushan["liushanwins"]
            liushanlosses=liushan["liushanlosses"]
            liushanmessage= "Wins: {}, Losses: {}" .format(liushanwins, liushanlosses)
        await interaction.response.send_message(liushanmessage)
    elif hero == "loong":
        with open('scriminfo.json', 'r') as file:
            loong=json.load(file)
            loongwins=loong["loongwins"]
            loonglosses=loong["loonglosses"]
            loongmessage= "Wins: {}, Losses: {}" .format(loongwins, loonglosses)
        await interaction.response.send_message(loongmessage)
    elif hero == "lubu":
        with open('scriminfo.json', 'r') as file:
            lubu=json.load(file)
            lubuwins=lubu["lubuwins"]
            lubulosses=lubu["lubulosses"]
            lubumessage= "Wins: {}, Losses: {}" .format(lubuwins, lubulosses)
        await interaction.response.send_message(lubumessage)
    elif hero == "luara":
        with open('scriminfo.json', 'r') as file:
            luara=json.load(file)
            luarawins=luara["luarawins"]
            luaralosses=luara["luaralosses"]
            luaramessage= "Wins: {}, Losses: {}" .format(luarawins, luaralosses)
        await interaction.response.send_message(luaramessage)
    elif hero == "luban":
        with open('scriminfo.json', 'r') as file:
            luban=json.load(file)
            lubanwins=luban["lubanwins"]
            lubanlosses=luban["lubanlosses"]
            lubanmessage= "Wins: {}, Losses: {}" .format(lubanwins, lubanlosses)
        await interaction.response.send_message(lubanmessage)
    elif hero == "luna":
        with open('scriminfo.json', 'r') as file:
            luna=json.load(file)
            lunawins=luna["lunawins"]
            lunalosses=luna["lunalosses"]
            lunamessage= "Wins: {}, Losses: {}" .format(lunawins, lunalosses)
        await interaction.response.send_message(lunamessage)
    elif hero == "mai":
        with open('scriminfo.json', 'r') as file:
            mai=json.load(file)
            maiwins=mai["maiwins"]
            mailosses=mai["mailosses"]
            maimessage= "Wins: {}, Losses: {}" .format(maiwins, mailosses)
        await interaction.response.send_message(maimessage)
    elif hero == "marco":
        with open('scriminfo.json', 'r') as file:
            marco=json.load(file)
            marcowins=marco["marcowins"]
            marcolosses=marco["marcolosses"]
            marcomessage= "Wins: {}, Losses: {}" .format(marcowins, marcolosses)
        await interaction.response.send_message(marcomessage)
    elif hero == "mayene":
        with open('scriminfo.json', 'r') as file:
            mayene=json.load(file)
            mayenewins=mayene["mayenewins"]
            mayenelosses=mayene["mayenelosses"]
            mayenemessage= "Wins: {}, Losses: {}" .format(mayenewins, mayenelosses)
        await interaction.response.send_message(mayenemessage)
    elif hero == "mengya":
        with open('scriminfo.json', 'r') as file:
            mengya=json.load(file)
            mengyawins=mengya["mengyawins"]
            mengyalosses=mengya["mengyalosses"]
            mengyamessage= "Wins: {}, Losses: {}" .format(mengyawins, mengyalosses)
        await interaction.response.send_message(mengyamessage)
    elif hero == "menki":
        with open('scriminfo.json', 'r') as file:
            menki=json.load(file)
            menkiwins=menki["menkiwins"]
            menkilosses=menki["menkilosses"]
            menkimessage= "Wins: {}, Losses: {}" .format(menkiwins, menkilosses)
        await interaction.response.send_message(menkimessage)
    elif hero == "miyue":
        with open('scriminfo.json', 'r') as file:
            miyue=json.load(file)
            miyuewins=miyue["miyuewins"]
            miyuelosses=miyue["miyuelosses"]
            miyuemessage= "Wins: {}, Losses: {}" .format(miyuewins, miyuelosses)
        await interaction.response.send_message(miyuemessage)
    elif hero == "milady":
        with open('scriminfo.json', 'r') as file:
            milady=json.load(file)
            miladywins=milady["miladywins"]
            miladylosses=milady["miladylosses"]
            miladymessage= "Wins: {}, Losses: {}" .format(miladywins, miladylosses)
        await interaction.response.send_message(miladymessage)
    elif hero == "ming":
        with open('scriminfo.json', 'r') as file:
            ming=json.load(file)
            mingwins=ming["mingwins"]
            minglosses=ming["minglosses"]
            mingmessage= "Wins: {}, Losses: {}" .format(mingwins, minglosses)
        await interaction.response.send_message(mingmessage)
    elif hero == "mozi":
        with open('scriminfo.json', 'r') as file:
            mozi=json.load(file)
            moziwins=mozi["moziwins"]
            mozilosses=mozi["mozilosses"]
            mozimessage= "Wins: {}, Losses: {}" .format(moziwins, mozilosses)
        await interaction.response.send_message(mozimessage)
    elif hero == "mulan":
        with open('scriminfo.json', 'r') as file:
            mulan=json.load(file)
            mulanwins=mulan["mulanwins"]
            mulanlosses=mulan["mulanlosses"]
            mulanmessage= "Wins: {}, Losses: {}" .format(mulanwins, mulanlosses)
        await interaction.response.send_message(mulanmessage)
    elif hero == "musashi":
        with open('scriminfo.json', 'r') as file:
            musashi=json.load(file)
            musashiwins=musashi["musashiwins"]
            musashilosses=musashi["musashilosses"]
            musashimessage= "Wins: {}, Losses: {}" .format(musashiwins, musashilosses)
        await interaction.response.send_message(musashimessage)
    elif hero == "nakoruru":
        with open('scriminfo.json', 'r') as file:
            nakoruru=json.load(file)
            nakoruruwins=nakoruru["nakoruruwins"]
            nakorurulosses=nakoruru["nakorurulosses"]
            nakorurumessage= "Wins: {}, Losses: {}" .format(nakoruruwins, nakorurulosses)
        await interaction.response.send_message(nakorurumessage)
    elif hero == "nezha":
        with open('scriminfo.json', 'r') as file:
            nezha=json.load(file)
            nezhawins=nezha["nezhawins"]
            nezhalosses=nezha["nezhalosses"]
            nezhamessage= "Wins: {}, Losses: {}" .format(nezhawins, nezhalosses)
        await interaction.response.send_message(nezhamessage)
    elif hero == "nuwa":
        with open('scriminfo.json', 'r') as file:
            nuwa=json.load(file)
            nuwawins=nuwa["nuwawins"]
            nuwalosses=nuwa["nuwalosses"]
            nuwamessage= "Wins: {}, Losses: {}" .format(nuwawins, nuwalosses)
        await interaction.response.send_message(nuwamessage)
    elif hero == "pei":
        with open('scriminfo.json', 'r') as file:
            pei=json.load(file)
            peiwins=pei["peiwins"]
            peilosses=pei["peilosses"]
            peimessage= "Wins: {}, Losses: {}" .format(peiwins, peilosses)
        await interaction.response.send_message(peimessage)
    elif hero == "lanling":
        with open('scriminfo.json', 'r') as file:
            lanling=json.load(file)
            lanlingwins=lanling["lanlingwins"]
            lanlinglosses=lanling["lanlinglosses"]
            lanlingmessage= "Wins: {}, Losses: {}" .format(lanlingwins, lanlinglosses)
        await interaction.response.send_message(lanlingmessage)
    elif hero == "frost":
        with open('scriminfo.json', 'r') as file:
            frost=json.load(file)
            frostwins=frost["frostwins"]
            frostlosses=frost["frostlosses"]
            frostmessage= "Wins: {}, Losses: {}" .format(frostwins, frostlosses)
        await interaction.response.send_message(frostmessage)
    elif hero == "sakeer":
        with open('scriminfo.json', 'r') as file:
            sakeer=json.load(file)
            sakeerwins=sakeer["sakeerwins"]
            sakeerlosses=sakeer["sakeerlosses"]
            sakeermessage= "Wins: {}, Losses: {}" .format(sakeerwins, sakeerlosses)
        await interaction.response.send_message(sakeermessage)
    elif hero == "shangguan":
        with open('scriminfo.json', 'r') as file:
            shangguan=json.load(file)
            shangguanwins=shangguan["shangguanwins"]
            shangguanlosses=shangguan["shangguanlosses"]
            shangguanmessage= "Wins: {}, Losses: {}" .format(shangguanwins, shangguanlosses)
        await interaction.response.send_message(shangguanmessage)
    elif hero == "shi":
        with open('scriminfo.json', 'r') as file:
            shi=json.load(file)
            shiwins=shi["shiwins"]
            shilosses=shi["shilosses"]
            shimessage= "Wins: {}, Losses: {}" .format(shiwins, shilosses)
        await interaction.response.send_message(shimessage)
    elif hero == "shouyue":
        with open('scriminfo.json', 'r') as file:
            shouyue=json.load(file)
            shouyuewins=shouyue["shouyuewins"]
            shouyuelosses=shouyue["shouyuelosses"]
            shouyuemessage= "Wins: {}, Losses: {}" .format(shouyuewins, shouyuelosses)
        await interaction.response.send_message(shouyuemessage)
    elif hero == "simayi":
        with open('scriminfo.json', 'r') as file:
            simayi=json.load(file)
            simayiwins=simayi["simayiwins"]
            simayilosses=simayi["simayilosses"]
            simayimessage= "Wins: {}, Losses: {}" .format(simayiwins, simayilosses)
        await interaction.response.send_message(simayimessage)
    elif hero == "sunbin":
        with open('scriminfo.json', 'r') as file:
            sunbin=json.load(file)
            sunbinwins=sunbin["sunbinwins"]
            sunbinlosses=sunbin["sunbinlosses"]
            sunbinmessage= "Wins: {}, Losses: {}" .format(sunbinwins, sunbinlosses)
        await interaction.response.send_message(sunbinmessage)
    elif hero == "sunce":
        with open('scriminfo.json', 'r') as file:
            sunce=json.load(file)
            suncewins=sunce["suncewins"]
            suncelosses=sunce["suncelosses"]
            suncemessage= "Wins: {}, Losses: {}" .format(suncewins, suncelosses)
        await interaction.response.send_message(suncemessage)
    elif hero == "ukyo":
        with open('scriminfo.json', 'r') as file:
            ukyo=json.load(file)
            ukyowins=ukyo["ukyowins"]
            ukyolosses=ukyo["ukyolosses"]
            ukyomessage= "Wins: {}, Losses: {}" .format(ukyowins, ukyolosses)
        await interaction.response.send_message(ukyomessage)
    elif hero == "wukong":
        with open('scriminfo.json', 'r') as file:
            wukong=json.load(file)
            wukongwins=wukong["wukongwins"]
            wukonglosses=wukong["wukonglosses"]
            wukongmessage= "Wins: {}, Losses: {}" .format(wukongwins, wukonglosses)
        await interaction.response.send_message(wukongmessage)
    elif hero == "wuyan":
        with open('scriminfo.json', 'r') as file:
            wuyan=json.load(file)
            wuyanwins=wuyan["wuyanwins"]
            wuyanlosses=wuyan["wuyanlosses"]
            wuyanmessage= "Wins: {}, Losses: {}" .format(wuyanwins, wuyanlosses)
        await interaction.response.send_message(wuyanmessage)
    elif hero == "xiangyu":
        with open('scriminfo.json', 'r') as file:
            xiangyu=json.load(file)
            xiangyuwins=xiangyu["xiangyuwins"]
            xiangyulosses=xiangyu["xiangyulosses"]
            xiangyumessage= "Wins: {}, Losses: {}" .format(xiangyuwins, xiangyulosses)
        await interaction.response.send_message(xiangyumessage)
    elif hero == "xiaoqiao":
        with open('scriminfo.json', 'r') as file:
            xiaoqiao=json.load(file)
            xiaoqiaowins=xiaoqiao["xiaoqiaowins"]
            xiaoqiaolosses=xiaoqiao["xiaoqiaolosses"]
            xiaoqiaomessage= "Wins: {}, Losses: {}" .format(xiaoqiaowins, xiaoqiaolosses)
        await interaction.response.send_message(xiaoqiaomessage)
    elif hero == "xuance":
        with open('scriminfo.json', 'r') as file:
            xuance=json.load(file)
            xuancewins=xuance["xuancewins"]
            xuancelosses=xuance["xuancelosses"]
            xuancemessage= "Wins: {}, Losses: {}" .format(xuancewins, xuancelosses)
        await interaction.response.send_message(xuancemessage)
    elif hero == "yangjian":
        with open('scriminfo.json', 'r') as file:
            yangjian=json.load(file)
            yangjianwins=yangjian["yangjianwins"]
            yangjianlosses=yangjian["yangjianlosses"]
            yangjianmessage= "Wins: {}, Losses: {}" .format(yangjianwins, yangjianlosses)
        await interaction.response.send_message(yangjianmessage)
    elif hero == "yao":
        with open('scriminfo.json', 'r') as file:
            yao=json.load(file)
            yaowins=yao["yaowins"]
            yaolosses=yao["yaolosses"]
            yaomessage= "Wins: {}, Losses: {}" .format(yaowins, yaolosses)
        await interaction.response.send_message(yaomessage)
    elif hero == "yaria":
        with open('scriminfo.json', 'r') as file:
            yaria=json.load(file)
            yariawins=yaria["yariawins"]
            yarialosses=yaria["yarialosses"]
            yariamessage= "Wins: {}, Losses: {}" .format(yariawins, yarialosses)
        await interaction.response.send_message(yariamessage)
    elif hero == "ying":
        with open('scriminfo.json', 'r') as file:
            ying=json.load(file)
            yingwins=ying["yingwins"]
            yinglosses=ying["yinglosses"]
            yingmessage= "Wins: {}, Losses: {}" .format(yingwins, yinglosses)
        await interaction.response.send_message(yingmessage)
    elif hero == "yixing":
        with open('scriminfo.json', 'r') as file:
            yixing=json.load(file)
            yixingwins=yixing["yixingwins"]
            yixinglosses=yixing["yixinglosses"]
            yixingmessage= "Wins: {}, Losses: {}" .format(yixingwins, yixinglosses)
        await interaction.response.send_message(yixingmessage)
    elif hero == "yuhuan":
        with open('scriminfo.json', 'r') as file:
            yuhuan=json.load(file)
            yuhuanwins=yuhuan["yuhuanwins"]
            yuhuanlosses=yuhuan["yuhuanlosses"]
            yuhuanmessage= "Wins: {}, Losses: {}" .format(yuhuanwins, yuhuanlosses)
        await interaction.response.send_message(yuhuanmessage)
    elif hero == "zhangfei":
        with open('scriminfo.json', 'r') as file:
            zhangfei=json.load(file)
            zhangfeiwins=zhangfei["zhangfeiwins"]
            zhangfeilosses=zhangfei["zhangfeilosses"]
            zhangfeimessage= "Wins: {}, Losses: {}" .format(zhangfeiwins, zhangfeilosses)
        await interaction.response.send_message(zhangfeimessage)
    elif hero == "zhouyu":
        with open('scriminfo.json', 'r') as file:
            zhouyu=json.load(file)
            zhouyuwins=zhouyu["zhouyuwins"]
            zhouyulosses=zhouyu["zhouyulosses"]
            zhouyumessage= "Wins: {}, Losses: {}" .format(zhouyuwins, zhouyulosses)
        await interaction.response.send_message(zhouyumessage)
    elif hero == "zilong":
        with open('scriminfo.json', 'r') as file:
            zilong=json.load(file)
            zilongwins=zilong["zilongwins"]
            zilonglosses=zilong["zilonglosses"]
            zilongmessage= "Wins: {}, Losses: {}" .format(zilongwins, zilonglosses)
        await interaction.response.send_message(zilongmessage)
    elif hero == "ziya":
        with open('scriminfo.json', 'r') as file:
            ziya=json.load(file)
            ziyawins=ziya["ziyawins"]
            ziyalosses=ziya["ziyalosses"]
            ziyamessage= "Wins: {}, Losses: {}" .format(ziyawins, ziyalosses)
        await interaction.response.send_message(ziyamessage)
    else:
       await interaction.response.send_message("please input valid hero. if you did, try /loadherolist if you haven't yet.")

@bot.tree.command(name="winrate",description="calculate hero winrate in percentage")
async def winrate(interaction:discord.Interaction, hero:str):
    if hero == "agudo":
        with open('scriminfo.json', 'r') as file:
         agudo=json.load(file)
         agudowins=agudo["agudowins"]
         agudolosses=agudo["agudolosses"]
         if 0 < (agudowins+agudolosses):
            agudowinrate=(agudowins/(agudowins+agudolosses))*100
            await interaction.response.send_message(agudowinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "alessio":
        with open('scriminfo.json', 'r') as file:
         alessio=json.load(file)
         alessiowins=alessio["alessiowins"]
         alessiolosses=alessio["alessiolosses"]
         if 0 < (alessiowins+alessiolosses):
            alessiowinrate=(alessiowins/(alessiowins+alessiolosses))*100
            await interaction.response.send_message(alessiowinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "allain":
        with open('scriminfo.json', 'r') as file:
         allain=json.load(file)
         allainwins=allain["allainwins"]
         allainlosses=allain["allainlosses"]
         if 0 < (allainwins+allainlosses):
            allainwinrate=(allainwins/(allainwins+allainlosses))*100
            await interaction.response.send_message(allainwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "angela":
        with open('scriminfo.json', 'r') as file:
         angela=json.load(file)
         angelawins=angela["angelawins"]
         angelalosses=angela["angelalosses"]
         if 0 < (angelawins+angelalosses):
            angelawinrate=(angelawins/(angelawins+angelalosses))*100
            await interaction.response.send_message(angelawinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "arke":
        with open('scriminfo.json', 'r') as file:
         arke=json.load(file)
         arkewins=arke["arkewins"]
         arkelosses=arke["arkelosses"]
         if 0 < (arkewins+arkelosses):
            arkewinrate=(arkewins/(arkewins+arkelosses))*100
            await interaction.response.send_message(arkewinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "arli":
        with open('scriminfo.json', 'r') as file:
         arli=json.load(file)
         arliwins=arli["arliwins"]
         arlilosses=arli["arlilosses"]
         if 0 < (arliwins+arlilosses):
            arliwinrate=(arliwins/(arliwins+arlilosses))*100
            await interaction.response.send_message(arliwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "arthur":
        with open('scriminfo.json', 'r') as file:
         arthur=json.load(file)
         arthurwins=arthur["arthurwins"]
         arthurlosses=arthur["arthurlosses"]
         if 0 < (arthurwins+arthurlosses):
            arthurwinrate=(arthurwins/(arthurwins+arthurlosses))*100
            await interaction.response.send_message(arthurwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "ata":
        with open('scriminfo.json', 'r') as file:
         ata=json.load(file)
         atawins=ata["atawins"]
         atalosses=ata["atalosses"]
         if 0 < (atawins+atalosses):
            atawinrate=(atawins/(atawins+atalosses))*100
            await interaction.response.send_message(atawinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "athena":
        with open('scriminfo.json', 'r') as file:
         athena=json.load(file)
         athenawins=athena["athenawins"]
         athenalosses=athena["athenalosses"]
         if 0 < (athenawins+athenalosses):
            athenawinrate=(athenawins/(athenawins+athenalosses))*100
            await interaction.response.send_message(athenawinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "augran":
        with open('scriminfo.json', 'r') as file:
         augran=json.load(file)
         augranwins=augran["augranwins"]
         augranlosses=augran["augranlosses"]
         if 0 < (augranwins+augranlosses):
            augranwinrate=(augranwins/(augranwins+augranlosses))*100
            await interaction.response.send_message(augranwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "biron":
        with open('scriminfo.json', 'r') as file:
         biron=json.load(file)
         bironwins=biron["bironwins"]
         bironlosses=biron["bironlosses"]
         if 0 < (bironwins+bironlosses):
            bironwinrate=(bironwins/(bironwins+bironlosses))*100
            await interaction.response.send_message(bironwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "butterfly":
        with open('scriminfo.json', 'r') as file:
         butterfly=json.load(file)
         butterflywins=butterfly["butterflywins"]
         butterflylosses=butterfly["butterflylosses"]
         if 0 < (butterflywins+butterflylosses):
            butterflywinrate=(butterflywins/(butterflywins+butterflylosses))*100
            await interaction.response.send_message(butterflywinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "caiyan":
        with open('scriminfo.json', 'r') as file:
         caiyan=json.load(file)
         caiyanwins=caiyan["caiyanwins"]
         caiyanlosses=caiyan["caiyanlosses"]
         if 0 < (caiyanwins+caiyanlosses):
            caiyanwinrate=(caiyanwins/(caiyanwins+caiyanlosses))*100
            await interaction.response.send_message(caiyanwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "charlotte":
        with open('scriminfo.json', 'r') as file:
         charlotte=json.load(file)
         charlottewins=charlotte["charlottewins"]
         charlottelosses=charlotte["charlottelosses"]
         if 0 < (charlottewins+charlottelosses):
            charlottewinrate=(charlottewins/(charlottewins+charlottelosses))*100
            await interaction.response.send_message(charlottewinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "cirrus":
        with open('scriminfo.json', 'r') as file:
         cirrus=json.load(file)
         cirruswins=cirrus["cirruswins"]
         cirruslosses=cirrus["cirruslosses"]
         if 0 < (cirruswins+cirruslosses):
            cirruswinrate=(cirruswins/(cirruswins+cirruslosses))*100
            await interaction.response.send_message(cirruswinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "consortyu":
        with open('scriminfo.json', 'r') as file:
         consortyu=json.load(file)
         consortyuwins=consortyu["consortyuwins"]
         consortyulosses=consortyu["consortyulosses"]
         if 0 < (consortyuwins+consortyulosses):
            consortyuwinrate=(consortyuwins/(consortyuwins+consortyulosses))*100
            await interaction.response.send_message(consortyuwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "daqiao":
        with open('scriminfo.json', 'r') as file:
         daqiao=json.load(file)
         daqiaowins=daqiao["daqiaowins"]
         daqiaolosses=daqiao["daqiaolosses"]
         if 0 < (daqiaowins+daqiaolosses):
            daqiaowinrate=(daqiaowins/(daqiaowins+daqiaolosses))*100
            await interaction.response.send_message(daqiaowinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "daji":
        with open('scriminfo.json', 'r') as file:
         daji=json.load(file)
         dajiwins=daji["dajiwins"]
         dajilosses=daji["dajilosses"]
         if 0 < (dajiwins+dajilosses):
            dajiwinrate=(dajiwins/(dajiwins+dajilosses))*100
            await interaction.response.send_message(dajiwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "dharma":
        with open('scriminfo.json', 'r') as file:
         dharma=json.load(file)
         dharmawins=dharma["dharmawins"]
         dharmalosses=dharma["dharmalosses"]
         if 0 < (dharmawins+dharmalosses):
            dharmawinrate=(dharmawins/(dharmawins+dharmalosses))*100
            await interaction.response.send_message(dharmawinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "direnjie":
        with open('scriminfo.json', 'r') as file:
         direnjie=json.load(file)
         direnjiewins=direnjie["direnjiewins"]
         direnjielosses=direnjie["direnjielosses"]
         if 0 < (direnjiewins+direnjielosses):
            direnjiewinrate=(direnjiewins/(direnjiewins+direnjielosses))*100
            await interaction.response.send_message(direnjiewinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "dianwei":
        with open('scriminfo.json', 'r') as file:
         dianwei=json.load(file)
         dianweiwins=dianwei["dianweiwins"]
         dianweilosses=dianwei["dianweilosses"]
         if 0 < (dianweiwins+dianweilosses):
            dianweiwinrate=(dianweiwins/(dianweiwins+dianweilosses))*100
            await interaction.response.send_message(dianweiwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "diaochan":
        with open('scriminfo.json', 'r') as file:
         diaochan=json.load(file)
         diaochanwins=diaochan["diaochanwins"]
         diaochanlosses=diaochan["diaochanlosses"]
         if 0 < (diaochanwins+diaochanlosses):
            diaochanwinrate=(diaochanwins/(diaochanwins+diaochanlosses))*100
            await interaction.response.send_message(diaochanwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "dolia":
        with open('scriminfo.json', 'r') as file:
         dolia=json.load(file)
         doliawins=dolia["doliawins"]
         dolialosses=dolia["dolialosses"]
         if 0 < (doliawins+dolialosses):
            doliawinrate=(doliawins/(doliawins+dolialosses))*100
            await interaction.response.send_message(doliawinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "donghuang":
        with open('scriminfo.json', 'r') as file:
         donghuang=json.load(file)
         donghuangwins=donghuang["donghuangwins"]
         donghuanglosses=donghuang["donghuanglosses"]
         if 0 < (donghuangwins+donghuanglosses):
            donghuangwinrate=(donghuangwins/(donghuangwins+donghuanglosses))*100
            await interaction.response.send_message(donghuangwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "drbian":
        with open('scriminfo.json', 'r') as file:
         drbian=json.load(file)
         drbianwins=drbian["drbianwins"]
         drbianlosses=drbian["drbianlosses"]
         if 0 < (drbianwins+drbianlosses):
            drbianwinrate=(drbianwins/(drbianwins+drbianlosses))*100
            await interaction.response.send_message(drbianwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "dun":
        with open('scriminfo.json', 'r') as file:
         dun=json.load(file)
         dunwins=dun["dunwins"]
         dunlosses=dun["dunlosses"]
         if 0 < (dunwins+dunlosses):
            dunwinrate=(dunwins/(dunwins+dunlosses))*100
            await interaction.response.send_message(dunwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "dyadia":
        with open('scriminfo.json', 'r') as file:
         dyadia=json.load(file)
         dyadiawins=dyadia["dyadiawins"]
         dyadialosses=dyadia["dyadialosses"]
         if 0 < (dyadiawins+dyadialosses):
            dyadiawinrate=(dyadiawins/(dyadiawins+dyadialosses))*100
            await interaction.response.send_message(dyadiawinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "fang":
        with open('scriminfo.json', 'r') as file:
         fang=json.load(file)
         fangwins=fang["fangwins"]
         fanglosses=fang["fanglosses"]
         if 0 < (fangwins+fanglosses):
            fangwinrate=(fangwins/(fangwins+fanglosses))*100
            await interaction.response.send_message(fangwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "erin":
        with open('scriminfo.json', 'r') as file:
         erin=json.load(file)
         erinwins=erin["erinwins"]
         erinlosses=erin["erinlosses"]
         if 0 < (erinwins+erinlosses):
            erinwinrate=(erinwins/(erinwins+erinlosses))*100
            await interaction.response.send_message(erinwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "fuzi":
        with open('scriminfo.json', 'r') as file:
         fuzi=json.load(file)
         fuziwins=fuzi["fuziwins"]
         fuzilosses=fuzi["fuzilosses"]
         if 0 < (fuziwins+fuzilosses):
            fuziwinrate=(fuziwins/(fuziwins+fuzilosses))*100
            await interaction.response.send_message(fuziwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "ganmo":
        with open('scriminfo.json', 'r') as file:
         ganmo=json.load(file)
         ganmowins=ganmo["ganmowins"]
         ganmolosses=ganmo["ganmolosses"]
         if 0 < (ganmowins+ganmolosses):
            ganmowinrate=(ganmowins/(ganmowins+ganmolosses))*100
            await interaction.response.send_message(ganmowinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "gao":
        with open('scriminfo.json', 'r') as file:
         gao=json.load(file)
         gaowins=gao["gaowins"]
         gaolosses=gao["gaolosses"]
         if 0 < (gaowins+gaolosses):
            gaowinrate=(gaowins/(gaowins+gaolosses))*100
            await interaction.response.send_message(gaowinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "garo":
        with open('scriminfo.json', 'r') as file:
         garo=json.load(file)
         garowins=garo["garowins"]
         garolosses=garo["garolosses"]
         if 0 < (garowins+garolosses):
            garowinrate=(garowins/(garowins+garolosses))*100
            await interaction.response.send_message(garowinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "guanyu":
        with open('scriminfo.json', 'r') as file:
         guanyu=json.load(file)
         guanyuwins=guanyu["guanyuwins"]
         guanyulosses=guanyu["guanyulosses"]
         if 0 < (guanyuwins+guanyulosses):
            guanyuwinrate=(guanyuwins/(guanyuwins+guanyulosses))*100
            await interaction.response.send_message(guanyuwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "guiguzi":
        with open('scriminfo.json', 'r') as file:
         guiguzi=json.load(file)
         guiguziwins=guiguzi["guiguziwins"]
         guiguzilosses=guiguzi["guiguzilosses"]
         if 0 < (guiguziwins+guiguzilosses):
            guiguziwinrate=(guiguziwins/(guiguziwins+guiguzilosses))*100
            await interaction.response.send_message(guiguziwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "hanxin":
        with open('scriminfo.json', 'r') as file:
         hanxin=json.load(file)
         hanxinwins=hanxin["hanxinwins"]
         hanxinlosses=hanxin["hanxinlosses"]
         if 0 < (hanxinwins+hanxinlosses):
            hanxinwinrate=(hanxinwins/(hanxinwins+hanxinlosses))*100
            await interaction.response.send_message(hanxinwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "heino":
        with open('scriminfo.json', 'r') as file:
         heino=json.load(file)
         heinowins=heino["heinowins"]
         heinolosses=heino["heinolosses"]
         if 0 < (heinowins+heinolosses):
            heinowinrate=(heinowins/(heinowins+heinolosses))*100
            await interaction.response.send_message(heinowinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "houyi":
        with open('scriminfo.json', 'r') as file:
         houyi=json.load(file)
         houyiwins=houyi["houyiwins"]
         houyilosses=houyi["houyilosses"]
         if 0 < (houyiwins+houyilosses):
            houyiwinrate=(houyiwins/(houyiwins+houyilosses))*100
            await interaction.response.send_message(houyiwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "huangzhong":
        with open('scriminfo.json', 'r') as file:
         huangzhong=json.load(file)
         huangzhongwins=huangzhong["huangzhongwins"]
         huangzhonglosses=huangzhong["huangzhonglosses"]
         if 0 < (huangzhongwins+huangzhonglosses):
            huangzhongwinrate=(huangzhongwins/(huangzhongwins+huangzhonglosses))*100
            await interaction.response.send_message(huangzhongwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "jing":
        with open('scriminfo.json', 'r') as file:
         jing=json.load(file)
         jingwins=jing["jingwins"]
         jinglosses=jing["jinglosses"]
         if 0 < (jingwins+jinglosses):
            jingwinrate=(jingwins/(jingwins+jinglosses))*100
            await interaction.response.send_message(jingwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "kaizer":
        with open('scriminfo.json', 'r') as file:
         kaizer=json.load(file)
         kaizerwins=kaizer["kaizerwins"]
         kaizerlosses=kaizer["kaizerlosses"]
         if 0 < (kaizerwins+kaizerlosses):
            kaizerwinrate=(kaizerwins/(kaizerwins+kaizerlosses))*100
            await interaction.response.send_message(kaizerwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "kongming":
        with open('scriminfo.json', 'r') as file:
         kongming=json.load(file)
         kongmingwins=kongming["kongmingwins"]
         kongminglosses=kongming["kongminglosses"]
         if 0 < (kongmingwins+kongminglosses):
            kongmingwinrate=(kongmingwins/(kongmingwins+kongminglosses))*100
            await interaction.response.send_message(kongmingwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "kui":
        with open('scriminfo.json', 'r') as file:
         kui=json.load(file)
         kuiwins=kui["kuiwins"]
         kuilosses=kui["kuilosses"]
         if 0 < (kuiwins+kuilosses):
            kuiwinrate=(kuiwins/(kuiwins+kuilosses))*100
            await interaction.response.send_message(kuiwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "ladysun":
        with open('scriminfo.json', 'r') as file:
         ladysun=json.load(file)
         ladysunwins=ladysun["ladysunwins"]
         ladysunlosses=ladysun["ladysunlosses"]
         if 0 < (ladysunwins+ladysunlosses):
            ladysunwinrate=(ladysunwins/(ladysunwins+ladysunlosses))*100
            await interaction.response.send_message(ladysunwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "ladyzhen":
        with open('scriminfo.json', 'r') as file:
         ladyzhen=json.load(file)
         ladyzhenwins=ladyzhen["ladyzhenwins"]
         ladyzhenlosses=ladyzhen["ladyzhenlosses"]
         if 0 < (ladyzhenwins+ladyzhenlosses):
            ladyzhenwinrate=(ladyzhenwins/(ladyzhenwins+ladyzhenlosses))*100
            await interaction.response.send_message(ladyzhenwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "lam":
        with open('scriminfo.json', 'r') as file:
         lam=json.load(file)
         lamwins=lam["lamwins"]
         lamlosses=lam["lamlosses"]
         if 0 < (lamwins+lamlosses):
            lamwinrate=(lamwins/(lamwins+lamlosses))*100
            await interaction.response.send_message(lamwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "libai":
        with open('scriminfo.json', 'r') as file:
         libai=json.load(file)
         libaiwins=libai["libaiwins"]
         libailosses=libai["libailosses"]
         if 0 < (libaiwins+libailosses):
            libaiwinrate=(libaiwins/(libaiwins+libailosses))*100
            await interaction.response.send_message(libaiwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "lixin":
        with open('scriminfo.json', 'r') as file:
         lixin=json.load(file)
         lixinwins=lixin["lixinwins"]
         lixinlosses=lixin["lixinlosses"]
         if 0 < (lixinwins+lixinlosses):
            lixinwinrate=(lixinwins/(lixinwins+lixinlosses))*100
            await interaction.response.send_message(lixinwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "lianpo":
        with open('scriminfo.json', 'r') as file:
         lianpo=json.load(file)
         lianpowins=lianpo["lianpowins"]
         lianpolosses=lianpo["lianpolosses"]
         if 0 < (lianpowins+lianpolosses):
            lianpowinrate=(lianpowins/(lianpowins+lianpolosses))*100
            await interaction.response.send_message(lianpowinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "liang":
        with open('scriminfo.json', 'r') as file:
         liang=json.load(file)
         liangwins=liang["liangwins"]
         lianglosses=liang["lianglosses"]
         if 0 < (liangwins+lianglosses):
            liangwinrate=(liangwins/(liangwins+lianglosses))*100
            await interaction.response.send_message(liangwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "liubang":
        with open('scriminfo.json', 'r') as file:
         liubang=json.load(file)
         liubangwins=liubang["liubangwins"]
         liubanglosses=liubang["liubanglosses"]
         if 0 < (liubangwins+liubanglosses):
            liubangwinrate=(liubangwins/(liubangwins+liubanglosses))*100
            await interaction.response.send_message(liubangwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "liubei":
        with open('scriminfo.json', 'r') as file:
         liubei=json.load(file)
         liubeiwins=liubei["liubeiwins"]
         liubeilosses=liubei["liubeilosses"]
         if 0 < (liubeiwins+liubeilosses):
            liubeiwinrate=(liubeiwins/(liubeiwins+liubeilosses))*100
            await interaction.response.send_message(liubeiwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "liushan":
        with open('scriminfo.json', 'r') as file:
         liushan=json.load(file)
         liushanwins=liushan["liushanwins"]
         liushanlosses=liushan["liushanlosses"]
         if 0 < (liushanwins+liushanlosses):
            liushanwinrate=(liushanwins/(liushanwins+liushanlosses))*100
            await interaction.response.send_message(liushanwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "loong":
        with open('scriminfo.json', 'r') as file:
         loong=json.load(file)
         loongwins=loong["loongwins"]
         loonglosses=loong["loonglosses"]
         if 0 < (loongwins+loonglosses):
            loongwinrate=(loongwins/(loongwins+loonglosses))*100
            await interaction.response.send_message(loongwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "lubu":
        with open('scriminfo.json', 'r') as file:
         lubu=json.load(file)
         lubuwins=lubu["lubuwins"]
         lubulosses=lubu["lubulosses"]
         if 0 < (lubuwins+lubulosses):
            lubuwinrate=(lubuwins/(lubuwins+lubulosses))*100
            await interaction.response.send_message(lubuwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "luara":
        with open('scriminfo.json', 'r') as file:
         luara=json.load(file)
         luarawins=luara["luarawins"]
         luaralosses=luara["luaralosses"]
         if 0 < (luarawins+luaralosses):
            luarawinrate=(luarawins/(luarawins+luaralosses))*100
            await interaction.response.send_message(luarawinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "luban":
        with open('scriminfo.json', 'r') as file:
         luban=json.load(file)
         lubanwins=luban["lubanwins"]
         lubanlosses=luban["lubanlosses"]
         if 0 < (lubanwins+lubanlosses):
            lubanwinrate=(lubanwins/(lubanwins+lubanlosses))*100
            await interaction.response.send_message(lubanwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "luna":
        with open('scriminfo.json', 'r') as file:
         luna=json.load(file)
         lunawins=luna["lunawins"]
         lunalosses=luna["lunalosses"]
         if 0 < (lunawins+lunalosses):
            lunawinrate=(lunawins/(lunawins+lunalosses))*100
            await interaction.response.send_message(lunawinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "mai":
        with open('scriminfo.json', 'r') as file:
         mai=json.load(file)
         maiwins=mai["maiwins"]
         mailosses=mai["mailosses"]
         if 0 < (maiwins+mailosses):
            maiwinrate=(maiwins/(maiwins+mailosses))*100
            await interaction.response.send_message(maiwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "marco":
        with open('scriminfo.json', 'r') as file:
         marco=json.load(file)
         marcowins=marco["marcowins"]
         marcolosses=marco["marcolosses"]
         if 0 < (marcowins+marcolosses):
            marcowinrate=(marcowins/(marcowins+marcolosses))*100
            await interaction.response.send_message(marcowinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "mayene":
        with open('scriminfo.json', 'r') as file:
         mayene=json.load(file)
         mayenewins=mayene["mayenewins"]
         mayenelosses=mayene["mayenelosses"]
         if 0 < (mayenewins+mayenelosses):
            mayenewinrate=(mayenewins/(mayenewins+mayenelosses))*100
            await interaction.response.send_message(mayenewinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "mengya":
        with open('scriminfo.json', 'r') as file:
         mengya=json.load(file)
         mengyawins=mengya["mengyawins"]
         mengyalosses=mengya["mengyalosses"]
         if 0 < (mengyawins+mengyalosses):
            mengyawinrate=(mengyawins/(mengyawins+mengyalosses))*100
            await interaction.response.send_message(mengyawinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "menki":
        with open('scriminfo.json', 'r') as file:
         menki=json.load(file)
         menkiwins=menki["menkiwins"]
         menkilosses=menki["menkilosses"]
         if 0 < (menkiwins+menkilosses):
            menkiwinrate=(menkiwins/(menkiwins+menkilosses))*100
            await interaction.response.send_message(menkiwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "miyue":
        with open('scriminfo.json', 'r') as file:
         miyue=json.load(file)
         miyuewins=miyue["miyuewins"]
         miyuelosses=miyue["miyuelosses"]
         if 0 < (miyuewins+miyuelosses):
            miyuewinrate=(miyuewins/(miyuewins+miyuelosses))*100
            await interaction.response.send_message(miyuewinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "milady":
        with open('scriminfo.json', 'r') as file:
         milady=json.load(file)
         miladywins=milady["miladywins"]
         miladylosses=milady["miladylosses"]
         if 0 < (miladywins+miladylosses):
            miladywinrate=(miladywins/(miladywins+miladylosses))*100
            await interaction.response.send_message(miladywinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "ming":
        with open('scriminfo.json', 'r') as file:
         ming=json.load(file)
         mingwins=ming["mingwins"]
         minglosses=ming["minglosses"]
         if 0 < (mingwins+minglosses):
            mingwinrate=(mingwins/(mingwins+minglosses))*100
            await interaction.response.send_message(mingwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "mozi":
        with open('scriminfo.json', 'r') as file:
         mozi=json.load(file)
         moziwins=mozi["moziwins"]
         mozilosses=mozi["mozilosses"]
         if 0 < (moziwins+mozilosses):
            moziwinrate=(moziwins/(moziwins+mozilosses))*100
            await interaction.response.send_message(moziwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "mulan":
        with open('scriminfo.json', 'r') as file:
         mulan=json.load(file)
         mulanwins=mulan["mulanwins"]
         mulanlosses=mulan["mulanlosses"]
         if 0 < (mulanwins+mulanlosses):
            mulanwinrate=(mulanwins/(mulanwins+mulanlosses))*100
            await interaction.response.send_message(mulanwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "musashi":
        with open('scriminfo.json', 'r') as file:
         musashi=json.load(file)
         musashiwins=musashi["musashiwins"]
         musashilosses=musashi["musashilosses"]
         if 0 < (musashiwins+musashilosses):
            musashiwinrate=(musashiwins/(musashiwins+musashilosses))*100
            await interaction.response.send_message(musashiwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "nakoruru":
        with open('scriminfo.json', 'r') as file:
         nakoruru=json.load(file)
         nakoruruwins=nakoruru["nakoruruwins"]
         nakorurulosses=nakoruru["nakorurulosses"]
         if 0 < (nakoruruwins+nakorurulosses):
            nakoruruwinrate=(nakoruruwins/(nakoruruwins+nakorurulosses))*100
            await interaction.response.send_message(nakoruruwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "nezha":
        with open('scriminfo.json', 'r') as file:
         nezha=json.load(file)
         nezhawins=nezha["nezhawins"]
         nezhalosses=nezha["nezhalosses"]
         if 0 < (nezhawins+nezhalosses):
            nezhawinrate=(nezhawins/(nezhawins+nezhalosses))*100
            await interaction.response.send_message(nezhawinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "nuwa":
        with open('scriminfo.json', 'r') as file:
         nuwa=json.load(file)
         nuwawins=nuwa["nuwawins"]
         nuwalosses=nuwa["nuwalosses"]
         if 0 < (nuwawins+nuwalosses):
            nuwawinrate=(nuwawins/(nuwawins+nuwalosses))*100
            await interaction.response.send_message(nuwawinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "pei":
        with open('scriminfo.json', 'r') as file:
         pei=json.load(file)
         peiwins=pei["peiwins"]
         peilosses=pei["peilosses"]
         if 0 < (peiwins+peilosses):
            peiwinrate=(peiwins/(peiwins+peilosses))*100
            await interaction.response.send_message(peiwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "lanling":
        with open('scriminfo.json', 'r') as file:
         lanling=json.load(file)
         lanlingwins=lanling["lanlingwins"]
         lanlinglosses=lanling["lanlinglosses"]
         if 0 < (lanlingwins+lanlinglosses):
            lanlingwinrate=(lanlingwins/(lanlingwins+lanlinglosses))*100
            await interaction.response.send_message(lanlingwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "frost":
        with open('scriminfo.json', 'r') as file:
         frost=json.load(file)
         frostwins=frost["frostwins"]
         frostlosses=frost["frostlosses"]
         if 0 < (frostwins+frostlosses):
            frostwinrate=(frostwins/(frostwins+frostlosses))*100
            await interaction.response.send_message(frostwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "sakeer":
        with open('scriminfo.json', 'r') as file:
         sakeer=json.load(file)
         sakeerwins=sakeer["sakeerwins"]
         sakeerlosses=sakeer["sakeerlosses"]
         if 0 < (sakeerwins+sakeerlosses):
            sakeerwinrate=(sakeerwins/(sakeerwins+sakeerlosses))*100
            await interaction.response.send_message(sakeerwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "shangguan":
        with open('scriminfo.json', 'r') as file:
         shangguan=json.load(file)
         shangguanwins=shangguan["shangguanwins"]
         shangguanlosses=shangguan["shangguanlosses"]
         if 0 < (shangguanwins+shangguanlosses):
            shangguanwinrate=(shangguanwins/(shangguanwins+shangguanlosses))*100
            await interaction.response.send_message(shangguanwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "shi":
        with open('scriminfo.json', 'r') as file:
         shi=json.load(file)
         shiwins=shi["shiwins"]
         shilosses=shi["shilosses"]
         if 0 < (shiwins+shilosses):
            shiwinrate=(shiwins/(shiwins+shilosses))*100
            await interaction.response.send_message(shiwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "shouyue":
        with open('scriminfo.json', 'r') as file:
         shouyue=json.load(file)
         shouyuewins=shouyue["shouyuewins"]
         shouyuelosses=shouyue["shouyuelosses"]
         if 0 < (shouyuewins+shouyuelosses):
            shouyuewinrate=(shouyuewins/(shouyuewins+shouyuelosses))*100
            await interaction.response.send_message(shouyuewinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "simayi":
        with open('scriminfo.json', 'r') as file:
         simayi=json.load(file)
         simayiwins=simayi["simayiwins"]
         simayilosses=simayi["simayilosses"]
         if 0 < (simayiwins+simayilosses):
            simayiwinrate=(simayiwins/(simayiwins+simayilosses))*100
            await interaction.response.send_message(simayiwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "sunbin":
        with open('scriminfo.json', 'r') as file:
         sunbin=json.load(file)
         sunbinwins=sunbin["sunbinwins"]
         sunbinlosses=sunbin["sunbinlosses"]
         if 0 < (sunbinwins+sunbinlosses):
            sunbinwinrate=(sunbinwins/(sunbinwins+sunbinlosses))*100
            await interaction.response.send_message(sunbinwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "sunce":
        with open('scriminfo.json', 'r') as file:
         sunce=json.load(file)
         suncewins=sunce["suncewins"]
         suncelosses=sunce["suncelosses"]
         if 0 < (suncewins+suncelosses):
            suncewinrate=(suncewins/(suncewins+suncelosses))*100
            await interaction.response.send_message(suncewinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "ukyo":
        with open('scriminfo.json', 'r') as file:
         ukyo=json.load(file)
         ukyowins=ukyo["ukyowins"]
         ukyolosses=ukyo["ukyolosses"]
         if 0 < (ukyowins+ukyolosses):
            ukyowinrate=(ukyowins/(ukyowins+ukyolosses))*100
            await interaction.response.send_message(ukyowinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "wukong":
        with open('scriminfo.json', 'r') as file:
         wukong=json.load(file)
         wukongwins=wukong["wukongwins"]
         wukonglosses=wukong["wukonglosses"]
         if 0 < (wukongwins+wukonglosses):
            wukongwinrate=(wukongwins/(wukongwins+wukonglosses))*100
            await interaction.response.send_message(wukongwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "wuyan":
        with open('scriminfo.json', 'r') as file:
         wuyan=json.load(file)
         wuyanwins=wuyan["wuyanwins"]
         wuyanlosses=wuyan["wuyanlosses"]
         if 0 < (wuyanwins+wuyanlosses):
            wuyanwinrate=(wuyanwins/(wuyanwins+wuyanlosses))*100
            await interaction.response.send_message(wuyanwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "xiangyu":
        with open('scriminfo.json', 'r') as file:
         xiangyu=json.load(file)
         xiangyuwins=xiangyu["xiangyuwins"]
         xiangyulosses=xiangyu["xiangyulosses"]
         if 0 < (xiangyuwins+xiangyulosses):
            xiangyuwinrate=(xiangyuwins/(xiangyuwins+xiangyulosses))*100
            await interaction.response.send_message(xiangyuwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "xiaoqiao":
        with open('scriminfo.json', 'r') as file:
         xiaoqiao=json.load(file)
         xiaoqiaowins=xiaoqiao["xiaoqiaowins"]
         xiaoqiaolosses=xiaoqiao["xiaoqiaolosses"]
         if 0 < (xiaoqiaowins+xiaoqiaolosses):
            xiaoqiaowinrate=(xiaoqiaowins/(xiaoqiaowins+xiaoqiaolosses))*100
            await interaction.response.send_message(xiaoqiaowinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "xuance":
        with open('scriminfo.json', 'r') as file:
         xuance=json.load(file)
         xuancewins=xuance["xuancewins"]
         xuancelosses=xuance["xuancelosses"]
         if 0 < (xuancewins+xuancelosses):
            xuancewinrate=(xuancewins/(xuancewins+xuancelosses))*100
            await interaction.response.send_message(xuancewinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "yangjian":
        with open('scriminfo.json', 'r') as file:
         yangjian=json.load(file)
         yangjianwins=yangjian["yangjianwins"]
         yangjianlosses=yangjian["yangjianlosses"]
         if 0 < (yangjianwins+yangjianlosses):
            yangjianwinrate=(yangjianwins/(yangjianwins+yangjianlosses))*100
            await interaction.response.send_message(yangjianwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "yao":
        with open('scriminfo.json', 'r') as file:
         yao=json.load(file)
         yaowins=yao["yaowins"]
         yaolosses=yao["yaolosses"]
         if 0 < (yaowins+yaolosses):
            yaowinrate=(yaowins/(yaowins+yaolosses))*100
            await interaction.response.send_message(yaowinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "yaria":
        with open('scriminfo.json', 'r') as file:
         yaria=json.load(file)
         yariawins=yaria["yariawins"]
         yarialosses=yaria["yarialosses"]
         if 0 < (yariawins+yarialosses):
            yariawinrate=(yariawins/(yariawins+yarialosses))*100
            await interaction.response.send_message(yariawinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "ying":
        with open('scriminfo.json', 'r') as file:
         ying=json.load(file)
         yingwins=ying["yingwins"]
         yinglosses=ying["yinglosses"]
         if 0 < (yingwins+yinglosses):
            yingwinrate=(yingwins/(yingwins+yinglosses))*100
            await interaction.response.send_message(yingwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "yixing":
        with open('scriminfo.json', 'r') as file:
         yixing=json.load(file)
         yixingwins=yixing["yixingwins"]
         yixinglosses=yixing["yixinglosses"]
         if 0 < (yixingwins+yixinglosses):
            yixingwinrate=(yixingwins/(yixingwins+yixinglosses))*100
            await interaction.response.send_message(yixingwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "yuhuan":
        with open('scriminfo.json', 'r') as file:
         yuhuan=json.load(file)
         yuhuanwins=yuhuan["yuhuanwins"]
         yuhuanlosses=yuhuan["yuhuanlosses"]
         if 0 < (yuhuanwins+yuhuanlosses):
            yuhuanwinrate=(yuhuanwins/(yuhuanwins+yuhuanlosses))*100
            await interaction.response.send_message(yuhuanwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "zhangfei":
        with open('scriminfo.json', 'r') as file:
         zhangfei=json.load(file)
         zhangfeiwins=zhangfei["zhangfeiwins"]
         zhangfeilosses=zhangfei["zhangfeilosses"]
         if 0 < (zhangfeiwins+zhangfeilosses):
            zhangfeiwinrate=(zhangfeiwins/(zhangfeiwins+zhangfeilosses))*100
            await interaction.response.send_message(zhangfeiwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "zhouyu":
        with open('scriminfo.json', 'r') as file:
         zhouyu=json.load(file)
         zhouyuwins=zhouyu["zhouyuwins"]
         zhouyulosses=zhouyu["zhouyulosses"]
         if 0 < (zhouyuwins+zhouyulosses):
            zhouyuwinrate=(zhouyuwins/(zhouyuwins+zhouyulosses))*100
            await interaction.response.send_message(zhouyuwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "zilong":
        with open('scriminfo.json', 'r') as file:
         zilong=json.load(file)
         zilongwins=zilong["zilongwins"]
         zilonglosses=zilong["zilonglosses"]
         if 0 < (zilongwins+zilonglosses):
            zilongwinrate=(zilongwins/(zilongwins+zilonglosses))*100
            await interaction.response.send_message(zilongwinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    elif hero == "ziya":
        with open('scriminfo.json', 'r') as file:
         ziya=json.load(file)
         ziyawins=ziya["ziyawins"]
         ziyalosses=ziya["ziyalosses"]
         if 0 < (ziyawins+ziyalosses):
            ziyawinrate=(ziyawins/(ziyawins+ziyalosses))*100
            await interaction.response.send_message(ziyawinrate)
         else:
            await interaction.response.send_message("no games found. unable to compute")
    else:
        await interaction.response.send_message("invalid hero.")


bot.run(TOKEN)
