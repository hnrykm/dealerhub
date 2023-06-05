import React, {useState, useEffect} from 'react';

function ManufacturerForm() {
    const handleSubmit = async (event) => {
        event.preventDefault();

        const data = {};
        data.name = name;

        const url = "http://localhost:8100/api/manufacturers/";
        const fetchConfig = {
            method:"post",
            body: JSON.stringify(data),
            headers: {
                "Conent-Type": "application/json",
            }
        }
        const response = await fetch (url, fetchConfig);
        if (response.ok) {
            const newManufacturer = await response.json();
            console.groupCollapsed(newManufacturer);
            setName('');
        };
    }

    const[name, setName] = useState('');
    const handleNameChange = (event) => {
        const value = event.target.value
        setName(value);
    }

    useEffect(() => {
        fetchData();
    }, []);

    return(
        <div className="row">
        <div className="offset-3 col-6">
            <div className="shadow p-4 mt-4">
                <h1>Create a manufacturer</h1>
                <form onSubmit={handleSubmit} id="create-manufacturer-form">
                    <div className="form-floating mb-3">
                        <input
                        onChange={handleNameChange}
                        value={name}
                        placeholder="Manufacturer name..."
                        type="text"
                        required
                        name="name"
                        id="name"
                        className="form-control"
                        />
                    </div>
                    <button className="btn btn-primary">Create</button>
                </form>
            </div>
        </div>
        </div>
    )

}

export default ManufacturerForm;