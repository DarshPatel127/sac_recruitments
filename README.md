# SAC Recruitment Product API

A simple Django REST Framework project for managing products. You can add, view, update, and delete products. Filtering and pagination are included.

## Setup

1. Clone this repo:
   ```bash
   git clone 
   cd sac_recruitment
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Migrate the database:
   ```bash
   python manage.py migrate
   ```

4. Make an admin user:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `GET /api/viewproducts/` — See all products (supports filtering & pagination)
- `POST /api/createproduct/` — Add a product
- `GET /api/viewproduct/<id>/` — Get a product by its ID
- `PUT /api/updateproduct/<id>/` — Update a product
- `DELETE /api/deleteproduct/<id>/` — Delete a product

### Filtering & Pagination
- You can use: `min_price`, `max_price`, `param` (search by name)
- Pagination: `?page=1`, `?page=2`, etc.

## Testing

To run the tests:
```bash
python manage.py test product_api
```

## API Docs
- Swagger UI: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- OpenAPI schema: [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

## Admin Panel
- [http://localhost:8000/admin/](http://localhost:8000/admin/)
- Log in with your superuser

## Notes
- All API endpoints are CSRF-exempt so you can test in Postman without issues.
- Default page size is 10 (change it in `settings.py` if you want).


