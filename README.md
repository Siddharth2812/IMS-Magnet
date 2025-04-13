# Magnet Backend API Documentation

This document provides detailed information about the API endpoints available in the Magnet Backend system.

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Initial Setup
1. Clone the repository
```bash
git clone <repository-url>
cd magnet
```

2. Create and activate virtual environment
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Apply database migrations
```bash
python manage.py migrate
```

5. Create a superuser (admin)
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

The server will start at http://127.0.0.1:8000/

### Development Guide

#### Project Structure
```
magnet/
├── magnet_backend/        # Main project directory
│   ├── settings.py        # Project settings
│   └── urls.py           # Main URL configuration
├── supplier_details/      # Supplier app
│   ├── models.py         # Supplier data models
│   ├── views.py          # API views
│   └── urls.py           # URL routing
├── master_material_list/  # Material app
│   ├── models.py         # Material data models
│   ├── views.py          # API views
│   └── urls.py           # URL routing
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

#### Creating New Models
1. Create/modify models in `your_app/models.py`:
```python
from django.db import models

class YourModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    
    class Meta:
        verbose_name = "Your Model"
        verbose_name_plural = "Your Models"
```

2. Create and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Adding New Views/Routes
1. Create API views in `your_app/views.py`:
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def your_view(request):
    if request.method == 'GET':
        # Handle GET request
        return Response(data)
    elif request.method == 'POST':
        # Handle POST request
        return Response(data, status=201)
```

2. Add URL patterns in `your_app/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('api/your-endpoint/', views.your_view, name='your-view'),
]
```

3. Include app URLs in `magnet_backend/urls.py`:
```python
from django.urls import path, include

urlpatterns = [
    path('', include('your_app.urls')),
]
```

#### Common Development Tasks

1. Create a new app:
```bash
python manage.py startapp your_app_name
```

2. Register app in `magnet_backend/settings.py`:
```python
INSTALLED_APPS = [
    ...
    'your_app_name',
]
```

3. Create admin interface in `your_app/admin.py`:
```python
from django.contrib import admin
from .models import YourModel

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2']
    search_fields = ['field1']
```

4. Run tests:
```bash
python manage.py test
```

5. Shell for debugging:
```bash
python manage.py shell
```

## Base URL
```
http://127.0.0.1:8000
```

## API Endpoints

### Supplier Details API

#### 1. List All Suppliers
- **URL:** `/api/suppliers/`
- **Method:** `GET`
- **Success Response:**
  ```json
  [
    {
      "model": "supplier_details.supplier",
      "pk": 1,
      "fields": {
        "supplier_name": "ABC Electronics",
        "address_line1": "123 Tech Street",
        "address_line2": "Industrial Area",
        "address_line3": "",
        "address_line4": "",
        "state": "Karnataka",
        "state_code": "KA",
        "payment_terms": "",
        "pan_no": "ABCDE1234F",
        "gst_no": "29ABCDE1234F1Z5",
        "igst": "18.00",
        "cgst": "9.00",
        "sgst": "9.00",
        "total_gst": "18.00",
        "contact_person": "John Doe",
        "phone_no": "9876543210",
        "email": "john@abcelectronics.com",
        "email_1": "",
        "bank_name": "",
        "branch": "",
        "account_no": "",
        "ifsc_code": "",
        "vendor_code": "ABC001"
      }
    }
  ]
  ```

#### 2. Create New Supplier
- **URL:** `/api/suppliers/`
- **Method:** `POST`
- **Required Fields:**
  - supplier_name (string)
  - state (string)
  - state_code (string)
  - pan_no (string, 10 chars)
  - gst_no (string, 15 chars)
  - vendor_code (string, unique)
- **Optional Fields:**
  - address_line1, address_line2, address_line3, address_line4 (string)
  - payment_terms (string)
  - igst, cgst, sgst, total_gst (decimal)
  - contact_person (string)
  - phone_no (string)
  - email, email_1 (email)
  - bank_name, branch, account_no, ifsc_code (string)
- **Sample Request Body:**
  ```json
  {
    "supplier_name": "ABC Electronics",
    "address_line1": "123 Tech Street",
    "state": "Karnataka",
    "state_code": "KA",
    "pan_no": "ABCDE1234F",
    "gst_no": "29ABCDE1234F1Z5",
    "igst": 18.00,
    "cgst": 9.00,
    "sgst": 9.00,
    "total_gst": 18.00,
    "vendor_code": "ABC001"
  }
  ```
- **Success Response:** Same format as GET response with status 201

#### 3. Get Specific Supplier
- **URL:** `/api/suppliers/<id>/`
- **Method:** `GET`
- **Success Response:** Same format as List response but for single supplier

#### 4. Update Supplier
- **URL:** `/api/suppliers/<id>/`
- **Method:** `PUT`
- **Request Body:** Same format as Create
- **Success Response:** Updated supplier data

#### 5. Delete Supplier
- **URL:** `/api/suppliers/<id>/`
- **Method:** `DELETE`
- **Success Response:** Status 204 No Content

### Master Material List API

#### 1. List All Materials
- **URL:** `/api/materials/`
- **Method:** `GET`
- **Success Response:**
  ```json
  [
    {
      "model": "master_material_list.mastermaterial",
      "pk": 1,
      "fields": {
        "vendor": 1,
        "description": "Power Resistor 100W",
        "part_no": "RES-100W-01",
        "unit": "PCS",
        "supplier_rate": "80.00",
        "seipl_rate": "95.00",
        "category": "Electronics",
        "sub_category": "Resistors",
        "sale_rate": "110.00",
        "total_received_qty": "500.00",
        "vendor_issued_qty": "0.00",
        "vendor_received_qty": "0.00",
        "board_issue_qty": "100.00",
        "avl_stock": "400.00",
        "avl_stock_value": "32000.00",
        "billing_qty_diff": "400.00",
        "total_received_cost": "40000.00",
        "total_billed_cost": "0.00",
        "cost_diff": "40000.00"
      }
    }
  ]
  ```

#### 2. Create New Material
- **URL:** `/api/materials/`
- **Method:** `POST`
- **Required Fields:**
  - vendor (integer, valid supplier ID)
  - description (string)
  - part_no (string, unique)
  - unit (string)
  - supplier_rate (decimal)
  - seipl_rate (decimal)
  - sale_rate (decimal)
- **Optional Fields:**
  - category (string)
  - sub_category (string)
  - total_received_qty (decimal, default 0)
  - vendor_issued_qty (decimal, default 0)
  - vendor_received_qty (decimal, default 0)
  - board_issue_qty (decimal, default 0)
- **Sample Request Body:**
  ```json
  {
    "vendor": 1,
    "description": "Power Resistor 100W",
    "part_no": "RES-100W-01",
    "unit": "PCS",
    "supplier_rate": 80.00,
    "seipl_rate": 95.00,
    "category": "Electronics",
    "sub_category": "Resistors",
    "sale_rate": 110.00,
    "total_received_qty": 500,
    "board_issue_qty": 100
  }
  ```
- **Success Response:** Same format as GET response with status 201

#### 3. Get Specific Material
- **URL:** `/api/materials/<id>/`
- **Method:** `GET`
- **Success Response:** Same format as List response but for single material

#### 4. Update Material
- **URL:** `/api/materials/<id>/`
- **Method:** `PUT`
- **Request Body:** Same format as Create
- **Success Response:** Updated material data

#### 5. Delete Material
- **URL:** `/api/materials/<id>/`
- **Method:** `DELETE`
- **Success Response:** Status 204 No Content

## Error Responses

All endpoints may return the following error responses:

- **400 Bad Request:**
  ```json
  {
    "error": "Error message describing what went wrong"
  }
  ```
- **404 Not Found:**
  ```json
  {
    "detail": "Not found."
  }
  ```

## Important Notes

1. All POST and PUT requests must include the `Content-Type: application/json` header
2. The vendor_code field in Suppliers must be unique
3. The part_no field in Materials must be unique
4. When creating a Material, make sure the vendor ID exists
5. Decimal fields accept up to 2 decimal places
6. Some fields are automatically calculated on save:
   - avl_stock
   - avl_stock_value
   - billing_qty_diff
   - cost_diff

## Example cURL Commands

### Create Supplier
```bash
curl -X POST http://127.0.0.1:8000/api/suppliers/ \
-H "Content-Type: application/json" \
-d '{
    "supplier_name": "ABC Electronics",
    "address_line1": "123 Tech Street",
    "state": "Karnataka",
    "state_code": "KA",
    "pan_no": "ABCDE1234F",
    "gst_no": "29ABCDE1234F1Z5",
    "vendor_code": "ABC001"
}'
```

### Create Material
```bash
curl -X POST http://127.0.0.1:8000/api/materials/ \
-H "Content-Type: application/json" \
-d '{
    "vendor": 1,
    "description": "Power Resistor 100W",
    "part_no": "RES-100W-01",
    "unit": "PCS",
    "supplier_rate": 80.00,
    "seipl_rate": 95.00,
    "sale_rate": 110.00
}'
```

### Get All Suppliers
```bash
curl http://127.0.0.1:8000/api/suppliers/
```

### Get All Materials
```bash
curl http://127.0.0.1:8000/api/materials/
``` 