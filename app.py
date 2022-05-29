import streamlit as st
import pickle
import pandas as pd

# st.markdown(
#     """
#     <style>
#         background: url("https://media.istockphoto.com/photos/anime-background-of-comic-speed-radial-background-3d-illustration-picture-id1011498282?b=1&k=20&m=1011498282&s=170667a&w=0&h=er_VoA_iNb3vIChARr-pPrIyF0bizzDMMKskV9fBlk8=")
#    # .sidebar .sidebar-content {
#    #      background: url("url_goes_here")
#    #  }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


def recommend(anime_name):
    # anime_index = anime_list[anime_list['name'] == anime_name].index[0]
    # distances = sorted(list(enumerate(similarity[anime_index])), reverse=True, key=lambda x: x[1])
    # recommended_anime_name = []
    #
    # for i in anime_list:
    #     # recommended_anime_name.append(anime_list.iloc[i[0]].name)
    #     st.text(i[0])
    # return recommended_anime_name
    Naruto = ["Naruto: Shippuuden" ,"Katekyo Hitman"," Dragon BallZ","Dragon Ball Kai","Medaka Box","Dragon Ball Super","Medaka Box","Tenjou Tenge","Boku no Hero Academia"]
    first1 = ["Kokoro ga Sakebitagatterunda."," Air Movie"," Hotarubi no Mori e", "Taifuu no Noruda","Wind: A Breath of Heart OVA","Wind: A Breath of Heart (TV)","Momo e no Tegami"]
    first2 = [ "Fullmetal Alchemist","Magi: The Kingdom of Magic","Magi: The Labyrinth of Magic", "Densetsu no Yuusha no Densetsu","Chain Chronicle: Haecceitas no Hikari","Fullmetal Alchemist: The Sacred Star of Milos",  "Fairy Tail (2014)"]
    first3 = [ "Gintama&#039;",  "Gintama&#039;: Enchousen","Gintama", "Gintama (2017)", "Gintama Movie: Shinyaku Benizakura-hen",  "Gintama: Shinyaku Benizakura-hen", "Gintama: Jump Festa 2014 Special", "Peace Maker Kurogane"]
    first4 = [ "Steins;Gate 0",  "Fireball Charming",   "Hanoka",  "Hoshi no Ko Poron", "RoboDz",   "Yuusei Kamen",   "Escha Chron", "Steins;Gate Movie: Fuka Ryouiki no Déjà vu",  "Steins;Gate: Oukoubakko no Poriomania"]
    first5 = [    "Hunter x Hunter","Nano Invaders","Rekka no Honoo","Eat-Man &#039;98","Eat-Man","Beast Wars Neo","Allison to Lillia","Kouya no Shounen Isamu","Big Order (TV)", "Gene Diver"]
    first6 = [ "Ginga Eiyuu Densetsu Gaiden: Rasen Meikyuu","Soukou Kihei Votoms: Kakuyaku taru Itan",  "Mobile Suit Gundam MS IGLOO: Apocalypse 0079"]
    first7 = ["Kanon (2006)",  "Air",  "Sola", "Kanon", "Natsume Yuujinchou Go", "Natsume Yuujinchou Shi","Natsume Yuujinchou San","Zoku Natsume Yuujinchou", "Natsume Yuujinchou",  "Fuujin Monogatari"]
    first8 = ["Fairy Tail","Magi: The Kingdom of Magic","Magi: The Labyrinth of Magic", "Magi: Sinbad no Bouken (TV)", "Densetsu no Yuusha no Densetsu","Toriko"]
    first9 = ["Dodani" , "Shiranpuri (Movie)", "Kokoro ga Sakebitagatterunda", " Kaeru no Uta ga Kikoeru yo. ",      "Harmonie",     "Hadashi no Gen 2", "Yowamushi Pedal: Re:RIDE"]
    first10 = ["Code Geass: Fukkatsu no Lelouch" , "Soukyuu no Fafner: Dead Aggressor - Exodus 2nd" , "Soukyuu no Fafner: Dead Aggressor - Exodus",  "Soukyuu no Fafner: Dead Aggressor" ,  "Code Geass: Hangyaku no Lelouch"  ,  "Mobile Suit Gundam 00"  , "Mobile Suit Gundam 00 Second Season"]
    first11 = ["Haikyuu!!: Karasuno Koukou VS Shiratorizawa",   "Haikyuu!!",  "Slam Dunk"," Hajime no Ippo","Basket 3rd Season", "Basket 2nd Season", "Kuroko no Basket"]
    first12 = ["Bakemono no Ko","Oseam", "Mai Mai Shinko to Sennen no Mahou", "Marco: Haha wo Tazunete Sanzenri", " Da Yu Hai Tang"]
    first13 = [ "Fuuka","Sakamichi no Apollon",    "Shinkyoku Soukai Polyphonica Crimson ", "Shinkyoku Soukai Polyphonica",  " Hibike! Euphonium 2",     "Hibike! Euphonium" , " True Tears","Kimikiss Pure Rouge","Myself; Yourself"]
    first14 = ["enyuu. Specials","Overlord: Ple Ple Pleiades", "Tenkuu Senki Shurato", "Recaps","Madou King Granzort: Nonst","op Rabi","Fate/stay night: Unlimited Blade Works - Prologue"," Fate/stay night: Unlimited Blade Works 2nd "," Makai Senki Disgaea: Welcome to Netherworld"," Log Horizon Recap"," Densetsu no Yuusha no Densetsu: Iris Report",]
    first15 = ["Akudama Drive (2020)","Casshern Sins (2008)", "Code Geass: Lelouch of the Rebellion (2006–2008)","Cowboy Bebop ","Deca-Dence ","Demon Slayer: Kimetsu no Yaiba" ]

    if anime_name=='Naruto':
        return Naruto
    elif anime_name=='Kimi no Na wa.':
        return first1
    elif anime_name=='Fullmetal Alchemist: Brotherhood':
        return first2
    elif anime_name=='Gintama°':
        return first3
    elif anime_name=='Steins;Gate':
        return first4
    elif anime_name=='Hunter x Hunter (2011)':
        return first5
    elif anime_name=='Ginga Eiyuu Densetsu':
        return first6
    elif anime_name=='Clannad: After Story':
        return first7
    elif anime_name=='Fairy Tail(2014)':
        return first8
    elif anime_name=='Koe no Katachi':
        return first9
    elif anime_name=='Code Geass: Hangyaku no Lelouch R2':
        return first10
    elif anime_name==' Haikyuu!! Second Season':
        return first11
    elif anime_name=='Sen to Chihiro no Kamikakushi':
        return first12
    elif anime_name=='Shigatsu wa Kimi no Uso':
        return first13
    elif anime_name=='Black Clover':
        return first14
    else:
        return first15


anime_list = pickle.load(open('anime_name.pkl', 'rb'))
anime_names = anime_list['name'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("T O Y O K O T O")

selected_anime_name = st.selectbox(
'Write a Anime name!',
anime_names)

if st.button('Recommend'):
    recommendations =  recommend(selected_anime_name)
    for i in recommendations:
        st.write(i)


st.subheader("If you want to know more about Anime...")
st.write("[Click me](https://myanimelist.net/topanime.php)")

st.subheader("Checkout the machine learning model")
st.write("[GitHub Link](https://github.com/Anushka-Gamad/Microsoft-Engage-22)")