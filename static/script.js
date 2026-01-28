//ensure JS runs after HTML fully load
document.addEventListener("DOMContentLoaded", ()=>{
    //select the form
    const form = document.getElementById("expense-form"); //const to declare form variable

    //function to load and display expenses
async function loadExpenses(){
    try{
        const response = await fetch("/expenses");
        const expenses = await response.json();

        const container = document.getElementById("expenses-list");
        container.innerHTML = ""; //clear previous content

        if(expenses.length === 0){
            container.textContent = "No expenses recorded.";
            return;
        }

        //create list items for each expense
        const ul = document.createElement("ul");
        expenses.forEach(exp=>{
            const li = document.createElement("li");
            li.textContent = `${exp.title} - $${exp.amount} - ${exp.date}`;
            ul.appendChild(li); //add list item to ul
        });

        container.appendChild(ul);
    } catch(error){
        console.error("Error fetching expenses:", error); //if try fails, then catch
    }
}

    loadExpenses(); //load existing expenses on page load

    //listen for form submission
    form.addEventListener("submit", async(event)=>{
        event.preventDefault(); //prevent default page reload

        //Grab values from inputs
        const title = document.getElementById("title").value;
        const amount = parseFloat(document.getElementById("amount").value); //convert to number
        const date = document.getElementById("date").value;

        try{
            const response = await fetch('/expenses', {
                method: "POST",
                headers:{
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({title, amount, date})
            });

            const result = await response.json();
            document.getElementById("message").textContent = result.message; //show success message

            loadExpenses(); //refresh the expenses list
        } catch(error) {
            console.error("Error:", error);
            document.getElementById("message").textContent = "An error occured!";
        }
    });
});



