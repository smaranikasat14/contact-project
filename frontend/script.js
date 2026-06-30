const form = document.getElementById("contactForm");
form.addEventListener("submit", async function(event) {
    event.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        subject: document.getElementById("subject").value,
        message: document.getElementById("message").value,
    };

    const response = await fetch("http://127.0.0.1:8000/contact",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(data)
                }
            );
        const result = await response.json();
        alert(result.message);
        form.reset();

        loadContacts(); 
    }
);

 async function loadContacts() {
        const response = await fetch("http://127.0.0.1:8000/contacts");
        const contacts = await response.json();

        console.log(contacts);
        console.log(Array.isArray(contacts));

        let output = "";

        contacts.forEach(contact => {
            output += `
                <div>
                    <h3>${contact[1]}</h3>
                    <p>Email: ${contact[2]}</p>
                    <p>Phone: ${contact[3]}</p>
                    <p>Subject: ${contact[4]}</p>
                    <p>Message: ${contact[5]}</p>
                    <button onclick="deleteContact(${contact[0]})">Delete</button>
                </div>
            `;
        });

        document.getElementById("contactList").innerHTML = output;
    }

loadContacts();

async function deleteContact(id) {
    await fetch(`http://127.0.0.1:8000/contact/${id}`, {
        method: "DELETE"
    });

    loadContacts();
}
