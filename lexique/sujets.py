import lexique.excludeWord as exclude
import re

def cleanUrl(url):
	regex = u"http://www.jeuxvideo.com/forums/42-51-[0-9]*-[0-9]*-[0-9]*-[0-9]*-[0-9]*-"
	url = re.sub(regex, '', url)
	url = url.replace(".htm", "")
	return url


def cleanMotsDic(motsDic):
	motsDic = {k: v for k, v in motsDic.items() if k not in exclude.words}
	motsDic = sorted(motsDic.items(), key=lambda t: t[1], reverse=True)
	return motsDic


def traitementUrl(url, motsDic):
	url = cleanUrl(url)
	motsUrl = url.split("-")
	for mot in motsUrl:
		if mot in motsDic:
			motsDic[mot] += 1
		else:
			motsDic[mot] = 1

	return motsDic


def traitementListUrl(urls, motsDic):
	for url in urls:
		motsDic = traitementUrl(url, motsDic)

	return motsDic


def occurenres(sujets):
	motsDic = {}
	urls = [x["url"] for x in sujets]
	motsDic = traitementListUrl(urls, motsDic)
	motsDic = cleanMotsDic(motsDic)
	return motsDic[0:30]





