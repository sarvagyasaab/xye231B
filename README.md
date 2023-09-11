RV_Connect
A brief description of RV_Connect.

## API Endpoints

This section provides an overview of the API endpoints available in our API.

| Endpoint                              | Description                                   |
| ------------------------------------- | --------------------------------------------- |
| `/api/users/`                         | List and create users                         |
| `/api/users/<int:pk>/`                | Retrieve, update, or delete a user by ID     |
| `/api/posts/`                         | List and create posts                         |
| `/api/posts/<int:pk>/`                | Retrieve, update, or delete a post by ID     |
| `/api/friendships/`                   | List and create friendships                   |
| `/api/friendships/<int:pk>/`          | Retrieve, update, or delete a friendship by ID |
| `/api/friend-requests/`               | List and create friend requests               |
| `/api/friend-requests/<int:pk>/`      | Retrieve, update, or delete a friend request by ID |
| `/api/users/search/?search=<query>`   | Search for users by username or email         |
| `/api-token-auth/`                    | Obtain an authentication token                |
| `/friend-requests/received/<str:user_identifier>/` | List received friend requests by user |
| `/friend-requests/sent/<str:user_identifier>/`     | List sent friend requests by user     |
| `/posts-by-user/<str:username>/`      | List posts by a specific user                |
| `/comments/<int:post_id>/`            | List comments for a specific post and create new comments |
