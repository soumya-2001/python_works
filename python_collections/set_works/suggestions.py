insta_users={"mohanlal","prithvi","dq","vijay","fahad","sureshgopi","lalu"}
mohanlal_following={"prithvi","vijay","lalu"}
mohanlal_suggestions=insta_users.difference(mohanlal_following)
mohanlal_suggestions.discard("mohanlal")
print(mohanlal_suggestions)

dq_following={"vijay","prithvi"}
mutual_friends=dq_following.intersection(mohanlal_following)
print(mutual_friends)