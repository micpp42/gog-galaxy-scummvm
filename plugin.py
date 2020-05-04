import sys, os, configparser, subprocess
from galaxy.api.plugin import Plugin, create_and_run_plugin
from galaxy.api.consts import Platform, LocalGameState
from galaxy.api.types import Authentication, Game, LicenseInfo, LicenseType, LocalGame

SCUMMVM_INSTALL_PATH = 'C:\\Program Files\\ScummVM\\scummvm.exe'
SCUMMVM_INI_PATH = os.path.join(os.getenv('appdata'), 'ScummVM\\scummvm.ini')


class PluginScummVM(Plugin):




    def __init__(self, reader, writer, token):
        super().__init__(
            Platform.Amiga,  # choose platform from available list
            "0.1",  # version
            reader,
            writer,
            token
        )


    def read_scummvm_ini_file(self):
        inifile = configparser.ConfigParser()
        inifile.read(SCUMMVM_INI_PATH)
        games = []
        for gameid in inifile.sections():
            if gameid not in ['scummvm','cloud']:
                games.append(Game(gameid,inifile[gameid]['description'].split(' (')[0],None, LicenseInfo(LicenseType.SinglePurchase)))

        return games





    async def authenticate(self, stored_credentials=None):
        user_data = {}
        user_data['username'] = 'ScummVM'
        self.store_credentials(user_data)
        return Authentication('scummvm', user_data['username'])


    async def get_owned_games(self):
        games = self.read_scummvm_ini_file()
        return games

    async def get_local_games(self):
        games = self.read_scummvm_ini_file()
        local_games = []
        for game in games:
            local_games.append(LocalGame(game.game_id, LocalGameState.Installed))
        return local_games


    async def launch_game(self, game_id):
        return subprocess.Popen([SCUMMVM_INSTALL_PATH,game_id])


def main():
    create_and_run_plugin(PluginScummVM, sys.argv)

# run plugin event loop
if __name__ == "__main__":
    main()
