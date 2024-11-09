// Variable to store slots data for each date
let slotsData = {
    today: ["10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM", "12:00 PM"],
    tomorrow: ["16:30 PM", "17:30 PM", "18:30 PM", "19:30 PM", "20:00 PM"],
    saturday: ["9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM"],
};

// Function to get the next Saturday
function getNextSaturday() {
    const today = new Date();
    const dayOfWeek = today.getDay();
    const daysUntilSaturday = (6 - dayOfWeek + 7) % 7;
    const nextSaturday = new Date(today);
    nextSaturday.setDate(today.getDate() + daysUntilSaturday);
    return nextSaturday;
}

// Function to generate date options dynamically
function generateDateOptions() {
    const dateSelector = document.getElementById('dateSelector');
    const today = new Date();
    const tomorrow = new Date(today);
    tomorrow.setDate(today.getDate() + 1);
    const nextSaturday = getNextSaturday();

    const options = [
        {
            label: today.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'short' }),
            value: "today",
            slots: slotsData.today
        },
        {
            label: tomorrow.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'short' }),
            value: "tomorrow",
            slots: slotsData.tomorrow
        },
        {
            label: nextSaturday.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'short' }),
            value: "saturday",
            slots: slotsData.saturday
        }
    ];

    // Create <option> elements dynamically and append to the dropdown
    options.forEach(option => {
        const opt = document.createElement('option');
        opt.value = option.value;
        opt.textContent = `${option.label} (${option.slots.length} Slots Available)`;
        dateSelector.appendChild(opt);
    });
}

// Function to update slots when a new date is selected
function updateSlots() {
    const selectedDate = document.getElementById('dateSelector').value;
    const slotsContainer = document.getElementById('slotsContainer');
    slotsContainer.innerHTML = ''; // Clear existing slots

    // Get the corresponding slots array for the selected date
    const selectedSlots = slotsData[selectedDate];

    if (selectedSlots && selectedSlots.length > 0) {
        selectedSlots.forEach(slot => {
            const slotButton = document.createElement('button');
            slotButton.classList.add('slot');
            slotButton.textContent = slot;

            // Add event listener to highlight the selected slot
            slotButton.addEventListener('click', () => {
                document.querySelectorAll('.slot').forEach(btn => btn.classList.remove('active-slot'));
                slotButton.classList.add('active-slot');
                selectedSlot = slotButton.innerText;
            });

            slotsContainer.appendChild(slotButton);
        });
    } else {
        slotsContainer.innerHTML = '<p>No slots available for this date</p>';
    }
}

// Call the function to generate the date options when the page loads
document.addEventListener('DOMContentLoaded', function() {
    generateDateOptions();
    updateSlots(); // Initialize slots for the first date
});

// Existing booking button code
let selectedSlot = null; // Variable to store the selected slot

document.getElementById('bookButton').addEventListener('click', function() {
    if (selectedSlot === null) {
        alert('Please choose a time slot before booking.');
    } else {
        // Booking confirmation code
        const button = this;
        const truck = document.getElementById('truck');
        const road = document.getElementById('roadMarkings');
        const buttonText = document.querySelector('.button-text');
        const orderText = document.querySelector('.order-text');

        truck.parentElement.style.display = 'flex';
        road.style.display = 'block';
        road.style.animation = 'roadAppear 1s linear forwards';

        setTimeout(() => {
            truck.style.animation = 'driveTruck 2.6s ease-in-out forwards';
            road.style.animation = 'roadDisappear 2.4s linear forwards';
        }, 1000);

        const bookNowText = "Booking...".split('');
        let delay = 0;
        buttonText.innerHTML = '';

        bookNowText.forEach((letter) => {
            let span = document.createElement('span');
            span.textContent = letter;
            span.style.display = 'inline-block';
            span.style.opacity = '1';
            buttonText.appendChild(span);

            setTimeout(() => {
                span.style.transition = 'opacity 2.7s ease';
                span.style.opacity = '0';
            }, delay);

            delay += 200;
        });

        const orderPlacedText = "Confirmed ✔".split('');
        orderText.textContent = '';
        orderText.style.display = 'inline-block';

        let truckProgressDelay = 1685;

        orderPlacedText.forEach((letter) => {
            let span = document.createElement('span');
            span.textContent = letter;
            span.style.display = 'inline-block';
            span.style.opacity = '0';
            orderText.appendChild(span);

            setTimeout(() => {
                span.style.transition = 'opacity 2.4s ease';
                span.style.opacity = '1';
            }, truckProgressDelay);

            truckProgressDelay += 100;
        });

        // Show confirmation popup after truck animation completes
        setTimeout(() => {
            showConfirmationPopup(); // Function to show confirmation popup
        }, 4000); // Delay the popup until after the truck finishes driving (adjust the timing as necessary)

        // Trigger email sending after booking confirmation
        sendEmailAfterBooking();  // Call this function to send email
    }
});

// Function to display the confirmation popup
function showConfirmationPopup() {
    const selectedDate = document.getElementById('dateSelector').value; // Get the selected date
    const selectedSlot = document.querySelector('.slot.active-slot').textContent; // Get the selected time slot

    // Create the popup container
    const popup = document.createElement('div');
    popup.className = 'confirmation-popup';
    
    // Popup content
    popup.innerHTML = `
        <div class="popup-content">
            <h2>Booking Confirmed</h2>
            <p>Your booking is confirmed for ${selectedDate} at ${selectedSlot}.</p>
            <button class="close-popup">Close</button>
        </div>
    `;
    
    // Append the popup to the body
    document.body.appendChild(popup);
    
    // Add event listener to close the popup
    document.querySelector('.close-popup').addEventListener('click', function() {
        popup.remove();
    });
}

// Function to send an email after booking
function sendEmailAfterBooking() {
    const selectedDate = document.getElementById('dateSelector').value;
    const selectedSlot = document.querySelector('.slot.active-slot').textContent;
    const doctorName = document.getElementById('doctorName').value;  // Doctor's name
    const doctorHospital = document.getElementById('doctorHospital').value;  // Doctor's hospital

    // Send the email with selected date, time, doctor name, and hospital
    fetch('/send_email', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            date: selectedDate, 
            time: selectedSlot, 
            doctor: doctorName, 
            hospital: doctorHospital 
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Log or display a confirmation message
    })
    .catch(error => console.error('Error sending email:', error));
}
// Function to trigger report generation
document.getElementById('generateReportBtn').addEventListener('click', function() {
    // Send an AJAX request to the Flask backend route that generates the PDF
    window.location.href = "/generate_report";
});
// CSS for the popup
const style = document.createElement('style');
style.innerHTML = `
    .confirmation-popup {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: white;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        z-index: 1000;
        border-radius: 8px;
    }
    .popup-content {
        text-align: center;
    }
    .popup-content h2 {
        margin-bottom: 10px;
    }
    .popup-content button {
        padding: 8px 16px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .popup-content button:hover {
        background-color: #0056b3;
    }
`;
document.head.appendChild(style);