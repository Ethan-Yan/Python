import fresh_tomatoes
import media

paycheck = media.Movie('Paycheck',
                       'A sci-fi thriller film',
                       'http://www.gstatic.com/tv/thumb/movieposters/33626/p33626_p_v8_aa.jpg',
                       'http://film.sohu.com/album/9069808.html?channeled=1200170003')
#print(paycheck.storyline)
sniper_legacy = media.Movie('Sniper: Legacy',
                     'A direct-to-video action film',
                     'http://www.gstatic.com/tv/thumb/movieposters/10978067/p10978067_p_v8_aa.jpg',
                     'http://film.sohu.com/album/8336254.html?channeled=1200170013')
#print(sniper_legacy.storyline)
#sniper_legacy.show_trailer()
killer_elite = media.Movie('Killer Elite', 'A British-Australian action thriller film',
                             'http://www.gstatic.com/tv/thumb/movieposters/8712034/p8712034_p_v8_as.jpg',
                             'http://film.sohu.com/album/7114730.html?channeled=1200170004')

unfaithful = media.Movie('Unfaithful', 'An American drama thriller film',
                          'http://www.gstatic.com/tv/thumb/dvdboxart/29634/p29634_d_v8_aa.jpg',
                          'http://film.sohu.com/album/8331636.html?channeled=1200160009')

captive = media.Movie('Captive', 'An American crime-drama thriller film',
                      'http://t2.gstatic.com/images?q=tbn:ANd9GcQN8ntsvLoT-Ds80G1h6RqXcIBrX2vDz07tv0H81jnm7KE6FwGg',
                      'http://film.sohu.com/album/9108619.html?channeled=1200160008')

the_condemned = media.Movie('The Condemned', 'An American action film',
                           'http://www.gstatic.com/tv/thumb/movieposters/163093/p163093_p_v8_aa.jpg',
                           'http://film.sohu.com/album/8384051.html?channeled=1200160011')

movies = [paycheck, sniper_legacy, killer_elite, unfaithful, captive, the_condemned]
fresh_tomatoes.open_movies_page(movies)
