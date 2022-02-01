import { useFormik } from 'formik';
import React from 'react';
import axios from "axios";

const SignupForm = () => {
  const formik = useFormik({
    initialValues: { email: ""},
    onSubmit: values => {
      alert(JSON.stringify(values, null, 2));
      axios({
          method: 'get',
          url: 'https://customervault-production.herokuapp.com/healthcheck',
          data: JSON.stringify(values),
        }).then((r) => {
          // setSubmitting(false);
          // resetForm();
          // setStatus('sent');
          console.log('Thanks!');
        });
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
