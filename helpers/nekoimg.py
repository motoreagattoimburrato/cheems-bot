import random
import nekos


def get_neko_sfw():
    possible = ['waifu', 'fox_girl', 'neko', 'cuddle']
    return nekos.img(random.choice(possible))


def get_neko_nsfw():
    possible = [
        'feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo',
        'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk',
        'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron',
        'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar',
        'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo',
        'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg',
        'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom',
        'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif',
        'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof']
    return nekos.img(random.choice(possible))


class NekoActions:
    def neko_slap():
        return nekos.img('slap')

    def neko_kiss():
        return nekos.img('kiss')

    def neko_pat():
        return nekos.img('pat')

    def neko_cuddle():
        return nekos.img('cuddle')


def owo_text(desired_text):
    return nekos.owoify(desired_text)