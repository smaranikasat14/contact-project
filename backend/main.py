from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import conn, cursor
from models import Contact

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/contact")
def create_contact(contact: Contact):

    cursor.execute(
        """
        INSERT INTO contact (name, email, phone, subject, message)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            contact.name,
            contact.email,
            contact.phone,
            contact.subject,
            contact.message
        )
    )

    conn.commit()

    return {
        "message": "Contact submitted successfully"
    }

@app.get("/contacts")
def get_contact():
    cursor.execute("SELECT * FROM contact")

    contacts = cursor.fetchall()

    return contacts

@app.delete("/contact/{id}")
def delete_contact(id: int):
    cursor.execute("DELETE FROM contact WHERE id=%s",(id,)
)
    conn.commit()

    return {"message": "Deleted Successfully"}


@app.put("/contact/{id}")
def update_contact(id: int, contact: Contact):

    cursor.execute(
        """
        UPDATE contact 
        SET
        name=%s,
        email=%s,
        phone=%s, 
        subject=%s, 
        message=%s
        WHERE id=%s
        """,
        (
            contact.name,
            contact.email,
            contact.phone,
            contact.subject,
            contact.message,
            id
        )
    )

    conn.commit()

    return {
        "message": "Contact updated successfully"
    }
