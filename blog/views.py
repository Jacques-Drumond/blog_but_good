from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.

def get_date(post):
    return post["date"]

all_posts = [
    {
        "slug": "hike-in-montains",
        "image": "montain.jpg",
        "author": "Jacques Drumond",
        "date": date(2023, 3, 30),
        "title": "Montain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the montains! And I was'nt prepared for what happend whilist I was enjoying the view!",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Nobis aliquam rem, 
            hic tempore similique veritatis deleniti possimus rerum at 
            ullam ipsa accusantium atque quia, aut numquam natus! Ex, animi in."""
    },
    {
        "slug": "in-the-woods",
        "image": "woods.jpg",
        "author": "Jacques Drumond",
        "date": date(2023, 1, 22),
        "title": "In the woods",
        "excerpt": "As we ventured further into the woods, we were enchanted by the diverse tapestry of flora and fauna that unfolded before our eyes",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Nobis aliquam rem, 
            hic tempore similique veritatis deleniti possimus rerum at 
            ullam ipsa accusantium atque quia, aut numquam natus! Ex, animi in."""
        
    },
    {
        "slug": "sea-fishing",
        "image": "seafishing.jpg",
        "author": "Jacques Drumond",
        "date": date(2023, 5, 10),
        "title": "Hooked on Thrills: Tales of Deep-Sea Fishing and Unexpected Encounters",
        "excerpt": "Join us as we set sail into the vast ocean and immerse ourselves in the exciting world of deep-sea fishing",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Nobis aliquam rem, 
            hic tempore similique veritatis deleniti possimus rerum at 
            ullam ipsa accusantium atque quia, aut numquam natus! Ex, animi in."""
    },
    {
        "slug": "culinary-delights",
        "image": "farm.jpeg",
        "author": "Jacques Drumond",
        "date": date(2023, 4, 11),
        "title": "From Farm to Fork: Exploring Gastronomic Adventures in Farm-to-Table Cooking",
        "excerpt": "Indulge your taste buds as we delve into the culinary realm of farm-to-table cooking.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Nobis aliquam rem, 
            hic tempore similique veritatis deleniti possimus rerum at 
            ullam ipsa accusantium atque quia, aut numquam natus! Ex, animi in."""
    },
    {
        "slug": "photography-expeditions-in-wildlife",
        "image": "wildlife.jpg",
        "author": "Jacques Drumond",
        "date": date(2023, 1, 19),
        "title": "Through the Lens: Capturing Wildlife's Majestic Moments in Photography Safaris",
        "excerpt": "Join us on awe-inspiring photography expeditions as we venture into the heart of wildlife habitats.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Nobis aliquam rem, 
            hic tempore similique veritatis deleniti possimus rerum at 
            ullam ipsa accusantium atque quia, aut numquam natus! Ex, animi in."""
    },
    {
        "slug": "finding-inner-peace",
        "image": "yoga.jpg",
        "author": "Jacques Drumond",
        "date": date(2023, 2, 27),
        "title": "Finding Inner Peace: Nurturing Mind and Body in Yoga and Meditation Retreats",
        "excerpt": "Embark on a transformative journey of self-discovery and relaxation as we explore the realm of yoga and meditation retreats",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Nobis aliquam rem, 
            hic tempore similique veritatis deleniti possimus rerum at 
            ullam ipsa accusantium atque quia, aut numquam natus! Ex, animi in."""
    }
]

def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts":latest_posts
})

def posts(request):
    return render(request, "blog/all_posts.html")

def post_detail(request, slug):
    return render(request, "blog/post_detail.html")