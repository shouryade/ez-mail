import { useState } from "preact/hooks";
import axios from "axios";

export function App() {
  const [formData, setFormData] = useState({
    username: "",
    phone: "",
    email: "",
  });
  const [succ, setSucc] = useState(false);

  const handleInputChange = (event, fieldName) => {
    setFormData({
      ...formData,
      [fieldName]: event.target.value,
    });
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post(
        "http://localhost:8000/api/users/create/",
        formData
      );
      console.log("Server response:", response.data);
      setSucc(true);
    } catch (error) {
      console.error("Error submitting data:", error);
    }
  };

  return (
    <>
      <div className="hero min-h-screen bg-base-200">
        <div className="hero-content text-center">
          <div className="max-w-md">
            <h1 className="card-title text-5xl font-bold text-center justify-center">
              Hello 👋
            </h1>
            <p className="py-2">
              <span className="text-2xl">Let us know who you are?</span>
              <br />
              <br />
              If you see this page, then the frontend has been set up properly!
              🥳
            </p>
            {succ ? (
              <div className="alert alert-success">
                <div className="flex-1">
                  <label>Success</label>
                  <p>Successfully submitted data!</p>
                </div>
              </div>
            ) : null}

            <div className="flex items-center flex-col space-y-4">
              <label htmlFor="username" className="text-accent">
                Username
              </label>
              <input
                type="text"
                id="username"
                className="input input-primary w-full max-w-xs"
                value={formData.username}
                onChange={(event) => handleInputChange(event, "username")}
              />

              <label htmlFor="phone" className="text-accent">
                Phone
              </label>
              <input
                type="text"
                id="phone"
                className="input input-primary w-full max-w-xs"
                value={formData.phone}
                onChange={(event) => handleInputChange(event, "phone")}
              />

              <label htmlFor="email" className="text-accent">
                Email
              </label>
              <input
                type="text"
                id="email"
                className="input input-primary w-full max-w-xs"
                value={formData.email}
                onChange={(event) => handleInputChange(event, "email")}
              />

              <button className="btn btn-primary" onClick={handleSubmit}>
                Submit😎
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
