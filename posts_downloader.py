from ph_py import ProductHuntClient

client_id = '<YOUR_APP_ID>'
client_secret = '<YOUR_APP_SECRET>'
redirect_uri = 'http://localhost:5000'
file_name = 'posts.csv'

daysBack = 600 #download posts for the last daysBack days

phc = ProductHuntClient(client_id, client_secret, redirect_uri)

with open(file_name, "a") as myfile:
    myfile.write('post_id,post_data,post_name,post_tagline,post_comments,post_votes,post_url,user_id,user_name,user_nickname')
    myfile.write('\n')
    for day in range(1,daysBack):
        print str(day)+" - ",
        for post in phc.get_previous_days_posts(day):
            print str(post.id),
            myfile.write(str(post.id))
            myfile.write(','+post.created_at)
            myfile.write(',\"'+post.name.encode('ascii', 'ignore').decode('ascii').replace('"','_')+'\"')
            myfile.write(',\"'+post.tagline.encode('ascii', 'ignore').decode('ascii').replace('"','_')+'\"')
            myfile.write(','+str(post.comments_count))
            myfile.write(','+str(post.votes_count))
            myfile.write(','+post.redirect_url)
            myfile.write(','+str(post.user.id))
            myfile.write(',\"'+post.user.name.encode('ascii', 'ignore').decode('ascii')+'\"')
            myfile.write(',\"'+post.user.username.encode('ascii', 'ignore').decode('ascii')+'\"')
            myfile.write('\n')
        print
myfile.close()