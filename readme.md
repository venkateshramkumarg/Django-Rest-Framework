# Django Rest Framework Blog API

A REST API project built with Django Rest Framework that provides CRUD operations for blog posts.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## Dependencies

- Django
- Django Rest Framework
- Other project-specific packages (listed in requirements.txt)

## API Endpoints

### Blog Posts
- `GET /api/blogs/` - List all blog posts
- `POST /api/blogs/` - Create a new blog post
- `GET /api/blogs/{id}/` - Retrieve a specific blog post
- `PUT /api/blogs/{id}/` - Update a blog post
- `DELETE /api/blogs/{id}/` - Delete a blog post

## Usage

Example API request:
```python
import requests

# List all blogs
response = requests.get('http://localhost:8000/api/blogs/')
blogs = response.json()

# Create a new blog post
new_blog = {
    'title': 'My Blog Post',
    'content': 'This is the content'
}
response = requests.post('http://localhost:8000/api/blogs/', json=new_blog)
```

## License

MIT License
