import { useFormik } from 'formik';
import React from 'react';
import ReactDOM from "react-dom"

const SignupForm = () => {
  const formik = useFormik({
    initialValues: { email: ""},
    onSubmit: values => {
      alert(JSON.stringify(values, null, 2));
    }
  });
  return (
    <form onSubmit={formik.handleSubmit}>
      <label htmlFor="email">Email Address</label>
      <input
        id="email"
        name="email"
        type="email"
        onChange={formik.handleChange}
        value={formik.values.email}
      />
      <button type="submit">Submit</button>
    </form>
  )
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <p>CustomerVault</p>
      </header>
      <SignupForm />
    </div>
  );
}

export default App;
