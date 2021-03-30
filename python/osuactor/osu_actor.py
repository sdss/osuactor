"""
import asyncio
import OSU_control as osu

from pymodbus3.client.sync import ModbusTcpClient as mbc
from clu import AMQPActor, command_parser


desi= osu.Controller()

@command_parser.command()
async def open(command):

    command.info(text="Opening the shutter!")
    # Here we would implement the actual communication
    await desi.exp_shutter('open')
    return command.finish(shutter="open")


@command_parser.command()
async def close(command):

    command.info(text="Closing the shutter!")
    # Here we would implement the actual communication
    await desi.exp_shutter('close')
    return command.finish(shutter="closed")

@command_parser.command()
async def telemetry(command):

    wago_status2, reply = await desi.getWAGOPower()
    wago_status1, reply = await desi.getWAGOEnv()
    if wago_status1 and wago_status2:
        command.info(text="Temperature & Humidity is:",status={
                "RH1(40001)":desi.sensors['40001'],
                "Temp1(40002)":desi.sensors['40002'],
                "RH2(40003)":desi.sensors['40003'],
                "Temp2(40004)":desi.sensors['40004'],
                "RH3(40005)":desi.sensors['40005'],
                "Temp3(40006)":desi.sensors['40006'],
                "RTD1(40009)":desi.sensors['40009'],
                "RTD2(40010)":desi.sensors['40010'],
                "RTD3(40011)":desi.sensors['40011'],
                "RTD4(40012)":desi.sensors['40012']
                })
        wagoClient = mbc(desi.wagoHost)
        rd = wagoClient.read_holding_registers(0,12)
        print(rd.registers)

    else:
        return command.fail(text=f"ERROR: Did not read sensors/powers")

    return command.finish()
                                             
class OsuActor(AMQPActor):
    def __init__(self):
            super().__init__(
            name="osu_actor",
            user="guest",
            password="guest",
            host="localhost",
            port=5672,
            version="0.1.0",
        )


async def run_actor():
    actor = await OsuActor().start()
    await actor.run_forever()

asyncio.run(run_actor())
"""
