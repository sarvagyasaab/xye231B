# API Documentation

This documentation provides a detailed overview of the endpoints in your Django application, including their URL patterns and functionality.

## Password Reset Endpoint

### URL Pattern
- `/password_reset/`

### Description
- This endpoint allows users to reset their passwords.

## User Search Endpoint

### URL Pattern
- `/api/users/search/`

### Description
- This endpoint is used to search for users based on their username or email.

### Request
- Method: GET
- URL: `/api/users/search/?search=<name>/<email>`

### Response
- Returns a list of users matching the search criteria.

## API Token Authentication Endpoint

### URL Pattern
- `/api-token-auth/`

### Description
- This endpoint is used for token-based authentication.

### Request
- Method: POST
- Data: User credentials (username and password)

### Response
- Returns an authentication token if the credentials are valid.

## Received Friend Requests Endpoint

### URL Pattern
- `/friend-requests/received/<str:user_identifier>/`

### Description
- This endpoint allows a user to view friend requests they have received.

### Request
- Method: GET
- URL: `/friend-requests/received/<str:user_identifier>/`

### Response
- Returns a list of friend requests received by the specified user.

## Sent Friend Requests Endpoint

### URL Pattern
- `/friend-requests/sent/<str:user_identifier>/`

### Description
- This endpoint allows a user to view friend requests they have sent.

### Request
- Method: GET
- URL: `/friend-requests/sent/<str:user_identifier>/`

### Response
- Returns a list of friend requests sent by the specified user.

## Posts by User Endpoint

### URL Pattern
- `/posts-by-user/<str:username>/`

### Description
- This endpoint allows you to retrieve posts made by a specific user.

### Request
- Method: GET
- URL: `/posts-by-user/<str:username>/`

### Response
- Returns a list of posts created by the specified user.

## Post Comments Endpoint

### URL Pattern
- `/comments/<int:post_id>/`

### Description
- This endpoint allows you to retrieve comments associated with a specific post and also create new comments for that post.

### Get Comments for a Post
#### Request
- Method: GET
- URL: `/comments/<int:post_id>/`

#### Response
- Returns a list of comments for the specified post.

### Create a Comment
#### Request
- Method: POST
- URL: `/comments/<int:post_id>/`
- Data: Comment content

#### Response
- Creates a new comment for the specified post.

## User Management Endpoints

These endpoints are used for user management, including user creation and listing users.

### User Creation Endpoint

#### URL Pattern
- `/api/users/`

#### Description
- This endpoint allows the creation of new users.

#### Request
- Method: POST
- Data: User details including username and password

#### Response
- Creates a new user if the provided data is valid.

### User Listing Endpoint

#### URL Pattern
- `/api/users/`

#### Description
- This endpoint lists all users in the system.

#### Request
- Method: GET
- URL: `/api/users/`

#### Response
- Returns a list of all users in the system.

## Friendship Endpoints

### Friendship Listing and Creation Endpoint

#### URL Pattern
- `/friendships/`

#### Description
- This endpoint lists all friendships in the system and allows the creation of new friendships.

#### Request
- Method: GET
- URL: `/friendships/`

#### Response
- Returns a list of all friendships in the system.

#### Request
- Method: POST
- Data: Friendship details including the users involved

#### Response
- Creates a new friendship if the provided data is valid.

## Friend Request Endpoints

### Friend Request Listing and Creation Endpoint

#### URL Pattern
- `/friend-requests/`

#### Description
- This endpoint lists all friend requests in the system and allows the creation of new friend requests.

#### Request
- Method: GET
- URL: `/friend-requests/`

#### Response
- Returns a list of all friend requests in the system.

#### Request
- Method: POST
- Data: Friend request details including the sender and receiver

#### Response
- Creates a new friend request if the provided data is valid.

### Accept/Reject Friend Request Endpoint

#### URL Pattern
- `/friend-requests/<int:request_id>/`

#### Description
- This endpoint allows the acceptance or rejection of a friend request.

#### Request
- Method: PATCH
- URL: `/friend-requests/<int:request_id>/`
- Data: Action (accept/reject)

#### Response
- Accepts or rejects the friend request based on the provided action.

## User Search Endpoint

### URL Pattern
- `/api/users/search/`

### Description
- This endpoint is used to search for users based on their username or email.

#### Request
- Method: GET
- URL: `/api/users/search/?search=<name>/<email>`

#### Response
- Returns a list of users matching the search criteria.

# Comments API Documentation

This API allows you to manage comments for posts. You can create, retrieve, update, and delete comments, as well as list comments for a specific post.

## Comments Endpoint

- Base URL: `/comments/`

### Create a Comment for a Post

**Endpoint:** `POST /comments/`

Create a new comment for a specific post.

#### Request Body

- `post_id` (integer, required): The ID of the post to which the comment belongs.
- `comment` (string, required): The text of the comment.
- `upvote` (boolean, optional): Indicates if the comment is upvoted (default: `false`).
- `downvote` (boolean, optional): Indicates if the comment is downvoted (default: `false`).

**Example Request:**

```json
POST /comments/
{
    "post_id": 1,
    "comment": "This is a great post!",
    "upvote": true
}
