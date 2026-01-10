
# Amenity API – Test Cases
---

### 1. Create Amenity – Success
<img width="938" height="310" alt="image" src="https://github.com/user-attachments/assets/7b473da8-8f7e-4f65-9888-985aaee8c877" />

### 2. Create Amenity – Missing Name
<img width="926" height="236" alt="image" src="https://github.com/user-attachments/assets/818275e8-31c4-47c8-845a-aa9c1f844c72" />

**Expected Result:**
- Status: `400 Bad Request`

```json
{
    "error": "Name is required and must be under 50 characters"
}
```

### 3. Create Amenity – Name Too Long (>50 chars)
<img width="920" height="338" alt="image" src="https://github.com/user-attachments/assets/426ead6f-39c8-4679-ba79-2ba0eaee761b" />


**Expected Result:**
- Status: `400 Bad Request`

```json
{
    "error": "Name is required and must be under 50 characters"
}
```
### 4. Get All Amenities – Success
<img width="929" height="290" alt="image" src="https://github.com/user-attachments/assets/c3919e41-7a37-46a1-adbb-bc54c7e9bd50" />


### 5. Get Amenity by ID – Success
<img width="931" height="234" alt="image" src="https://github.com/user-attachments/assets/9f6a23d9-c8ec-4e4d-9623-26e0e88c92be" />

### 6. Get Amenity by ID – Not Found
<img width="928" height="255" alt="image" src="https://github.com/user-attachments/assets/6a85938a-2236-45d8-9072-da7f45420c49" />


**Expected Result:**
- Status: `400 Bad Request`

```json
{
    "error": "Amenity not found"
}
```

### 7. Update Amenity – Success
<img width="924" height="322" alt="image" src="https://github.com/user-attachments/assets/439d66b2-a16b-4c1e-9518-8576bfe25789" />

### 8. Update Amenity – Not Found
<img width="937" height="256" alt="image" src="https://github.com/user-attachments/assets/5d701b20-d312-4127-a9fc-a10821cfc3e2" />

**Expected Result:**
- Status: `400 Bad Request`

```json
{
    "error": "Amenity not found"
}
```

### 9. Update Amenity – Invalid Data (Empty Name)
<img width="933" height="229" alt="image" src="https://github.com/user-attachments/assets/7d2b1e6a-2391-4bad-9887-47850a15bdf7" />

**Expected Result:**
- Status: `400 Bad Request`

```json
{
    "error": "Name is required and must be under 50 characters"
}
```

