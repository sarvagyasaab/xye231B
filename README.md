# API Endpoints and Views

| Endpoint                                  | View Class                      | Description                                          |
|-------------------------------------------|---------------------------------|------------------------------------------------------|
| `/posts/`                                | `PostViewSet`                  | Get a list of the top 100 posts ordered by date.    |
| `/friendships/`                          | `FriendshipViewSet`            | Get a list of all friendships.                       |
| `/posts/<str:username>/`                 | `PostViewSet.get_posts_by_user` | Retrieve all posts made by a specific user.         |
| `/friend_requests/<str:user_identifier>/` | `FriendRequestReceivedViewSet`  | Retrieve friend requests received by a user.        |
| `/friend_requests_sent/<str:user_identifier>/` | `FriendRequestSentViewSet`  | Retrieve friend requests sent by a user.          |

## View Descriptions

### `PostViewSet`
- **Description:** Provides endpoints to retrieve and manage posts.
- **Endpoints:**
  - `/posts/`: Get a list of the top 100 posts ordered by date.
  - `/posts/<str:username>/`: Retrieve all posts made by a specific user.

### `FriendshipViewSet`
- **Description:** Provides endpoints to retrieve and manage friendships.
- **Endpoints:**
  - `/friendships/`: Get a list of all friendships.

### `FriendRequestReceivedViewSet`
- **Description:** Provides endpoints to retrieve friend requests received by a user.
- **Endpoints:**
  - `/friend_requests/<str:user_identifier>/`: Retrieve friend requests received by the specified user.

### `FriendRequestSentViewSet`
- **Description:** Provides endpoints to retrieve friend requests sent by a user.
- **Endpoints:**
  - `/friend_requests_sent/<str:user_identifier>/`: Retrieve friend requests sent by the specified user.
