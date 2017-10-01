words = [
'0',
'1',
'10',
'18',
'2',
'25',
'3',
'4',
'5',
'51',
'6',
'7',
'a',
'a bas de',
'a cause de',
'a cote de',
'a defaut de ',
'a demi',
'a force de',
"a l'egard",
"a l'encontre de",
"a l'entour de",
"a l'exception de",
"a l'instar de",
"a l'insu de",
'a la faveur de',
'a la merci',
'a l’envi',
'a meme',
'a moins de',
'a partir de',
'a raison de',
'a seule fin de',
'a travers',
'a vau-l’eau',
'a vu',
'afin de',
'ai',
'ailleurs',
'ainsi',
'alentour',
'alerte',
'alias',
'alors',
'apres',
'après',
'après-demain',
'arrière',
'as',
'assez',
'au',
'au defaut de',
'au depens de',
'au lieu de',
'au moyen de',
'au prix de',
'au-dedans de',
'au-dehors',
'au-dela',
'au-dessous',
'au-dessous de',
'au-dessus',
'au-dessus de',
'au-devant',
'aucun',
'aucune',
'aucunes',
'aucuns',
"aujourd'hui",
'auparavant',
'aupres de',
'auprès',
'auquel',
'aussi',
'aussitôt',
'autant',
'autour',
'autour de',
'autre',
'autrefois',
'autres',
'autrui',
'aux',
'aux alentours de',
'aux environs de',
'auxquelles',
'auxquels',
'avant',
'avant de',
'avec',
'avex',
'avez',
'avoir',
'avons',
'b',
'beaucoup',
'bien',
'bientôt',
'bon gré',
'bref',
'c',
'ca',
'ce',
'ceci',
'cela',
'celle',
'celle-ci',
'celle-là',
'celles',
'celles-ci',
'celles-là',
'celui',
'celui-ci',
'celui-là',
'cependant',
'certain',
'certaine',
'certaines',
'certains',
'certes',
'ces',
'cet',
'cette',
'ceux',
'ceux-ci',
'ceux-là',
'chaque',
'chez',
'cinq',
'cinquante',
'combien',
'comment',
'concernant',
'contre',
'couci-couça',
'd',
"d'",
"d'abord",
"d'ailleurs",
"d'apres",
"d'autant",
"d'autres",
"d'avec",
"d'emblée",
"d'entre",
'dans',
'davantage',
'de',
'de façon a',
'de la',
'de la part de',
'de laquelle',
'de maniere a',
'de par',
'de peur de',
'de plain-pied',
'de visu',
'de-ci',
'de-la',
'debout',
'dedans',
'dehors',
'demain',
'depuis',
'derriere',
'des',
'desquelles',
'desquels',
'dessous',
'dessus',
'deux',
'deuxième',
'devant',
'différent',
'différente',
'différentes',
'différents',
'divers',
'diverse',
'diverses',
'dix',
'dont',
'dorénavant',
'douze',
'dru',
'du',
'du cote de',
'duquel',
'durant',
'dès',
'dès lors',
'déja',
'désormais',
'd’aucuns',
'e',
'elle',
'elles',
'en',
'en bas de',
'en deca de',
'en dedans de',
'en dehors de',
'en depit de',
'en face de',
'en faveur de',
'en guise de',
'en outre de',
'en plus de',
'en retrait',
'en tapinois',
'en travers',
'en vain',
'encore',
'enfin',
'ensemble',
'ensuite',
'entre',
'entre-temps',
'envers',
'environ',
'es',
'est',
'et',
'etait',
'etc',
'ete',
'etes',
'eux',
'ex nihilo',
'exprès',
'f',
'faire',
'fais',
'faisons',
'fait',
'faites',
'fois',
'font',
'g',
'grace a',
'gré',
'guère',
'h',
'hier',
'hormis',
'hors',
'hors de',
'http://www.jeuxvideo.com/forums/1',
'huit',
'i',
'ici',
'ici la',
'ici-bas',
'idem',
'il',
'ils',
'j',
'jadis',
'jamais',
'je',
'jusque',
'k',
'l',
"l'",
"l'autre",
"l'un",
"l'une",
'la',
'la contre',
'la leur',
'la meme',
'la mienne',
'la nôtre',
'la où',
'la plupart',
'la sienne',
'la tienne',
'la vôtre',
'la-bas',
'la-dedans',
'la-dessous',
'la-dessus',
'la-haut',
'laquelle',
'le',
'le leur',
'le meme',
'le mien',
'le nôtre',
'le sien',
'le tien',
'le vôtre',
'lequel',
'les',
'les autres',
'les leurs',
'les memes',
'les miennes',
'les miens',
'les nôtres',
'les siennes',
'les siens',
'les tiennes',
'les tiens',
'les unes',
'les uns',
'les vôtres',
'lesquelles',
'lesquels',
'leur',
'leurs',
'loin',
'loin de',
'lol',
'longtemps',
'lors',
'lors de',
'lorsque',
'lui',
'l’',
'm',
'ma',
'maint',
'mainte',
'maintenant',
'maintes',
'maints',
'mais',
'mal',
'malgre',
'malgré',
'me',
'meme',
'memes',
'merci',
'mes',
'mieux',
'moi',
'moins',
'mon',
'moyennant',
'm’',
'n',
'naguère',
'ne',
'neuf',
'non',
'nonobstant',
'nos',
'nos vos',
'notre',
'nous',
'nul',
'nulle',
'nulle part',
'nulles',
'nuls',
'néanmoins',
'o',
'on',
'ont',
'onze',
'ou',
'oui',
'outre',
'où',
'p',
'par',
'par la meme',
'par rapport a',
'par suite de',
'par-ci',
'par-dela',
'par-dessous',
'par-dessus',
'par-la',
'parfois',
'parmi',
'partout',
'pas',
'pendant',
'personne',
'peu',
'peut-etre',
'pile',
'pis',
'plein',
'plus',
'plusieurs',
'plutôt',
'point',
'pour',
'pourquoi',
'pourtant',
'premier',
'pres',
'pres de',
'presque',
'proche de',
'près',
'puis',
'q',
"qu'",
"qu'est-ce",
'quand',
'quant a',
'quarante',
'quatorze',
'quatre',
'que',
'quel',
'quel que',
'quelconque',
'quelconques',
'quelle',
'quelle que',
'quelles',
'quelles que',
"quelq'",
"quelqu'un",
"quelqu'une",
'quelque',
'quelquefois',
'quelques',
'quelques unes',
'quelques uns',
'quels',
'quels que',
'qui',
'quiconque',
'quinze',
'quitte a',
'quoi',
'quoique',
'r',
's',
'sa',
'sans',
'sans cesse',
'sauf',
'sauf a',
'se',
'seize',
'selon',
'sept',
'ses',
'si',
'sitôt',
'six',
'soi',
'sommes',
'son',
'sont',
'soudain',
'sous',
'sous couleur de',
'souvent',
'suis',
'suivant',
'sur',
'sur-le-champ',
'surtout',
'sus',
't',
'ta',
'tandis',
'tant',
'tant mieux',
'tant pis',
'tantôt',
'tard',
'te',
'tel',
'telle',
'tellement',
'telles',
'tels',
'tes',
'toi',
'ton',
'touchant',
'toujours',
'tous',
'tout',
'toute',
'toutefois',
'toutes',
'treize',
'trente',
'trois',
'troisième',
'trop',
'trop tard',
'trop tôt',
'très',
'très peu',
'tu',
'tôt',
't’',
'u',
'un',
'un autre',
'une',
'une autre',
'v',
'vers',
'via',
'vingt',
'vis-a-vie',
'vite',
'voici',
'voila',
'voire',
'volontiers',
'vos',
'votre',
'vous',
'w',
'x',
'y',
'z',
'à laquelle',
'ça',
'ça et la']