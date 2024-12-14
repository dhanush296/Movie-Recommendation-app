import tkinter as tk
import random

movies_by_genre = {
    "Action": ["Gabbar Singh", "Aravinda Sametha Veera Raghava", "Sahoo", "Akhanda", "Rangastalam", "Narappa"],
    "Comedy": ["Nuvvu Naaku Nachchav", "Pelli Choopulu", "Jathi Ratnalu", "Ee Nagaraniki Emaindi", "Tillu Square"],
    "Drama": ["Lucky Baskhar", "Devara", "Pratinidhi 2", "Pushpa: The Rule-2", "Oopiri", "C/o Kancharapalem"],
    "Horror": ["Masooda", "Virupaksha", "Maa Oori Polimera", "Kanchana", "Taxiwala", "Bhaagamathie"],
    "Sci-Fi": ["Aditya 369", "Kaliki 2898-AD", "Oke Oka Jeevitham", "Ismart Shankar", "Adbhutham", "Maanaadu"],
    "Family": ["Murari", "Srikaram", "Balagam", "F2", "Srimanthudu", "Seethamma Vakitlo Sirimalle Chettu", "Ala Vaikunthapurramuloo", "Samajavaragamana"],
    "Love": ["Orange", "Tholi Prema", "Kushi", "Sita Ramam", "Colour Photo", "Radhe Shyam", "Jaanu", "Shyam Singha Roy", "Arjun Reddy", "Joe","3"],
    "Thriller": ["Drishyam", "Hit", "Mathu Vadhalara", "Agent Sai Srinivasa Athreya", "Kshanam", "Rakshahudu", "V"],
    "Periodical": ["Bahubali-1&2", "Bimbisara", "Magadheera", "Gautamiputra Satakarni", "Rudhuramadevi", "Ghazi"],
    "Friendship": ["Happydays", "Vunnadi Okate Zindagi", "Yevade Subramanyam", "Maharshi", "Kerintha", "Devadas", "Kirrak party", "Aarya 1&2"]
}

def recommend_movie(genre, previous_recommendations):
    if genre in movies_by_genre:
        movies = movies_by_genre[genre][1:]
        movies = [movie for movie in movies if movie not in previous_recommendations]
        return random.choice(movies) if movies else "No more recommendations available."
    else:
        return "Sorry, we don't have any recommendations for that genre."

def show_recommendation():
    genre = genre_var.get()
    recommendation = recommend_movie(genre, previous_recommendations)
    result_label.config(text=recommendation)
    if recommendation != "No more recommendations available.":
        previous_recommendations.append(recommendation)
    satisfaction_frame.pack(pady=10)

def handle_satisfaction(satisfied):
    if satisfied:
        rate_frame.pack(pady=10)
    else:
        result_label.config(text="")
        satisfaction_frame.pack_forget()

def handle_rating(rating):
    result_label.config(text="")
    rate_frame.pack_forget()
    thank_you_label.config(text="Thanks for using the Movie Recommendation App!\nEnjoy the movie!")
    thank_you_label.pack(pady=10)

root = tk.Tk()
root.title("Movie Recommendation App")
root.geometry("400x400")

genre_var = tk.StringVar()
tk.Label(root, text="Select a genre:", font=('Arial', 14)).pack(pady=10)
tk.OptionMenu(root, genre_var, "Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Family", "Love", "Thriller", "Periodical", "Friendship").pack(pady=10)
tk.Button(root, text="Recommend a Movie", command=show_recommendation, font=('Arial', 14)).pack(pady=20)
result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack(pady=10)

satisfaction_frame = tk.Frame(root)
tk.Label(satisfaction_frame, text="Are you satisfied with the recommendation?", font=('Arial', 12)).pack(side=tk.LEFT)
tk.Button(satisfaction_frame, text="Yes", command=lambda: handle_satisfaction(True), font=('Arial', 12)).pack(side=tk.LEFT, padx=5)
tk.Button(satisfaction_frame, text="No", command=lambda: handle_satisfaction(False), font=('Arial', 12)).pack(side=tk.LEFT, padx=5)

rate_frame = tk.Frame(root)
tk.Label(rate_frame, text="Please rate the app:", font=('Arial', 12)).pack(side=tk.LEFT)
tk.Button(rate_frame, text="Bad", command=lambda: handle_rating("Bad"), font=('Arial', 12)).pack(side=tk.LEFT, padx=5)
tk.Button(rate_frame, text="Average", command=lambda: handle_rating("Average"), font=('Arial', 12)).pack(side=tk.LEFT, padx=5)
tk.Button(rate_frame, text="Good", command=lambda: handle_rating("Good"), font=('Arial', 12)).pack(side=tk.LEFT, padx=5)

thank_you_label = tk.Label(root, text="", font=('Arial', 14))

previous_recommendations = []

root.mainloop()
