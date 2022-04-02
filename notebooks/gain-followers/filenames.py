from pathlib import Path


# Use of parents1
data_path = Path.cwd().parents[1].joinpath('data')

#folders
raw_data_path = data_path.joinpath('raw')
log_data_path = raw_data_path.joinpath('log')
intermediate_data_path = data_path.joinpath('intermediate')
processed_data_path = data_path.joinpath('processed')
intermediate_users_path = intermediate_data_path.joinpath('users')

#profile
profile_folder_path = raw_data_path.joinpath('profile')
profile_path = profile_folder_path.joinpath('profile_')
gain_followers_folder_path = raw_data_path.joinpath('gain_followers')

#traveltrackie
traveltrackie_folder_path = raw_data_path.joinpath('traveltrackie')
traveltrackie_users_folder_path = traveltrackie_folder_path.joinpath('users')
traveltrackie_chunks_path = traveltrackie_folder_path.joinpath('chunks')
traveltrackie_extracted_todate_folder_path = traveltrackie_folder_path.joinpath('extracted_todate')

followers_path = traveltrackie_users_folder_path.joinpath('followers.txt')
followees_path = traveltrackie_users_folder_path.joinpath('followees.txt')
old_followers_path = traveltrackie_users_folder_path.joinpath('old_followers.txt')
new_followers_path = traveltrackie_users_folder_path.joinpath('new_followers.txt')
follow_unfollow_path = traveltrackie_users_folder_path.joinpath('follow_unfollow.txt')
inactive_path = traveltrackie_users_folder_path.joinpath('inactive.txt')
todate_path = traveltrackie_extracted_todate_folder_path.joinpath('usernames_todate.txt')
similar_accounts_path = traveltrackie_users_folder_path.joinpath('similar_accounts.txt')

#post
post_likes_path = traveltrackie_users_folder_path.joinpath('post_likes.txt')
new_post_likes_path = traveltrackie_users_folder_path.joinpath('new_post_likes.txt')

# others
others_folder_path = raw_data_path.joinpath('others')
others_users_folder_path = others_folder_path.joinpath('users')
others_followers_path = others_users_folder_path.joinpath('followers.txt')
others_chunks_path = others_folder_path.joinpath('chunks')
others_profile_folder_path = others_folder_path.joinpath('profile')
others_profile_path = others_profile_folder_path.joinpath('profile_')

log_path = log_data_path.joinpath('log_')
