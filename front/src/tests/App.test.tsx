import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders CustomerVault element', () => {
  render(<App />);
  const el = screen.getByText(/CustomerVault/i);
  expect(el).toBeInTheDocument();
});
