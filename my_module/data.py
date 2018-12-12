# Rock conversation
rock_convo_dict = {'FIRST_IN': ['hello', 'hi', 'hey', 'yo'],
                         'FIRST_OUT': ["Yo DROCK here, so you wanna talk about ROCK?"],

                         'GUITAR_IN': [ 'lead', 'elec', 'guitar', 'riff'],
                         'GUITAR_OUT': ["The greatest player was Jimi Hendrix",
										"I know that riff was crazy",
										"But I heard Gibson is the best",
										"I know I get it"],
										 
                         'BASS_IN': [ 'bass', 'bas', 'root', 'low'],
                         'BASS_OUT': ["I like Fender FA-135CE bass guitar!",
										"Dude, Jack Bruce from Metallica rules",
										"The Ornage Bass guitar amp looked nice",
										"You think we'll be as good as Flea?"],

                         'DRUM_IN': [ 'drum', 'beat', 'rhythm', 'tempo' ],
                         'DRUM_OUT': ["Yamaha 5 piece drum set are OK",
										"Bonem father and son legacy is the bomb",
										"You gotta wire that kick drum",
										"My drummer wont end the song!"],

                         'VOCAL_IN': ['freddie', 'mercury', 'vocal', 'singer', 'mic', 'mc', 'microphone'],
                         'VOCAL_OUT': ["Did you see the movie Queen? ",
										"Freddie Mercury plays piano really well",
										"But I like Ozzy Osbourne",
										"I heard SM90 microphone improved"],

                         'TOPCHART_IN': ['top', 'chart', 'billboard', 'favorite', 'good'],
                         'TOPCHART_OUT': ["Sweet Child O'Mine",
										"We Will Rock You",
										"Smells like Teen Spirit",
										"Walk This Way"],

                         'FAMOUS_IN': ['famous', 'million', 'eagles', 'rolling stones'],
                         'FAMOUS_OUT': ["I thought U2 was number 1 rock band",
										" sold millions of albums. that's crazy",
										"Surprisingly, Metallica is never been attained",
										"Did you know the Van Halen had daughter who went to college? "],
                         'FAMOUS_NAMES': {'eagles': 'most long lasting', 
										'rolling stones': 'the legend',
										'famous': 'ultimately',
										'million': 'extra'},

                         'DONOTLIKE_IN': ['bad', 'evil', 'sucks', 'hate', 'worst'],
                         'DONOTLIKE_OUT': ["yeah I hate them too",
										"Stop talking about that band!",
										"I think the worst band is Nickelback",
										"Man Kid Rock screw up again"],

                         'OTHERS': ['I think so too', 
										'Whatever',
										'Ok if you insist, man',
										'What was that!?',
										'Oh Hells no']
                         }

# Pop conversation
pop_convo_dict = {'FIRST_IN': ['hello', 'hi', 'hey', 'yo'],
                         'FIRST_OUT': ['Yo DROCK here, so you wanna talk about POP?'],

                         'GUITAR_IN': ['lead', 'elec', 'sound', 'mix'],
                         'GUITAR_OUT': ["They are all made up sound",
										"Mixed up pretty good",
										"I can't describe the sound lol",
										"Just Pure clarity!"],
										 
                         'BASS_IN': ['bass', 'bas', 'root', 'low'],
                         'BASS_OUT': ["Roland Synth AX09 rules!",
										"Synthesized bass from that song is crazy",
										"what is the frequency of the bass of that song",
										"You just cannot generate more bass"],

                         'DRUM_IN': [ 'drum', 'beat', 'rhythm', 'tempo'],
                         'DRUM_OUT': ["Maybe 120 BPM would work for it",
										"There is too much going on",
										"I know it was strange pregression",
										"The composer must cut down more beats"],

                         'VOCAL_IN': [ 'taylor', 'gaga', 'sing', 'microphone', 'vocal', 'song'],
                         'VOCAL_OUT': ["Yea I admire that singer too",
										"The fashion sense!",
										"oh no doubt, greatest vocal!",
										"well at least he is still alive"],

                         'TOPCHART_IN': ['top', 'chart', 'billboard', 'favorite', 'good'],
                         'TOPCHART_OUT': ["Hey Jude",
										"Uptown Funk"
										"Call Me Mabybe"
										"End of the Road"],

                         'FAMOUS_IN': ['famous', 'billboard', 'chart', 'million', 'gold', 'ultimate'],
                         'FAMOUS_OUT': ["But I love Taylor Swift? ",
										"Man, guess what, Mariah messed it up again",
										"Oh yeah that is one of the gold disk",
										"I know that's just crazy"],
                         'FAMOUS_NAMES': {'michael': 'Jackson', 'taylor': 'Swift'},

                         'DONOTLIKE_IN': ['bad', 'evil', 'sucks', 'hate', 'worst'],
                         'DONOTLIKE_OUT': ["yeah me dont like either",
										"Stop talking about it!",
										"I think the worst is Macarena",
										"Dude that's mean"],

                         'OTHERS': ['I think so too', 
										'Whatever',
										'Ok if you insist, man',
										'What was that!?',
										'Oh Hells no']
                         }

music_genre_interface = {
    'rock': rock_convo_dict,
    'pop': pop_convo_dict
}