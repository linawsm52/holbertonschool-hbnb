# Review API – Test Cases
---

### 1. Create Review – Success
<img width="919" height="478" alt="image" src="https://github.com/user-attachments/assets/ae7d2f35-2cf5-45d3-9ff7-8dfb7717163f" />



### 2. Create Review – Missing Required Field
missing rating
<img width="933" height="347" alt="image" src="https://github.com/user-attachments/assets/a794f5e2-55a3-42e1-91b7-9f87d7e4890d" />


**Expected Result:**
- Status: `400 Bad Request`

```json
{
  "error": "Invalid review data"
}
```

### 3. Create Review – Invalid Rating (Out of Range)
<img width="939" height="382" alt="image" src="https://github.com/user-attachments/assets/47d5de27-aa6b-4cd6-ab69-2d4bea95b659" />


**Expected Result:**
- Status: `400 Bad Request`

```json
"errors": {
    "error": "Rating must be 1-5"
  }
```
### 4. Create Review – User Does Not Exist
<img width="915" height="383" alt="image" src="https://github.com/user-attachments/assets/eaa25a60-85c9-4871-a530-0c061211fef9" />

**Expected Result:**
- Status: `400 Bad Request`

```json
{
  "error": "User not found"
}
```

### 5. Create Review – Place Does Not Exist
<img width="928" height="372" alt="image" src="https://github.com/user-attachments/assets/8b17d1d3-61dd-4948-ad48-35fb2388849b" />

**Expected Result:**
- Status: `400 Bad Request`

```json
{
  "error": "Place not found"
}
```

### 6. Get All Reviews – Success
<img width="939" height="336" alt="image" src="https://github.com/user-attachments/assets/715295dd-8976-4757-8a56-47cec370ead6" />
