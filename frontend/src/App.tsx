import React, { Component, KeyboardEventHandler } from 'react';
import './App.css';
import axios from 'axios';

import CreatableSelect from 'react-select/creatable';
import { OnChangeValue } from 'react-select';
import { Table } from "./components/Table";
import { Button, Container } from "@material-ui/core";
import { Condition } from "./type";

const components = {
  DropdownIndicator: null,
};
interface Option {
  readonly label: string;
  readonly value: string;
}

const createOption = (label: string) => ({
  label,
  value: label,
});

interface State {
  readonly inputValue: string;
  readonly selectedValues: readonly Option[];
  conditions: Condition[];
}
export default class App extends Component<{}, State> {
  state: State = {
    inputValue: '',
    selectedValues: [],
    conditions: [],
  };
  searchConditions = () => {
    const { selectedValues } = this.state;
    axios.post<Condition[]>('http://localhost:8000/api/diseases/', selectedValues).then(response => {
      this.setState({ conditions: response.data });
    });
  };
  handleChange = (
    selectedValues: OnChangeValue<Option, true>,
  ) => {
    this.setState({ selectedValues });
  };
  handleInputChange = (inputValue: string) => {
    this.setState({ inputValue });
  };
  handleKeyDown: KeyboardEventHandler<HTMLDivElement> = (event) => {
    const { inputValue, selectedValues } = this.state;
    if (!inputValue) return;
    switch (event.key) {
      case 'Enter':
      case 'Tab':
        this.setState({
          inputValue: '',
          selectedValues: [...selectedValues, createOption(inputValue)],
        });
        event.preventDefault();
    }
  };
  render() {
    const { inputValue, selectedValues, conditions } = this.state;
    return (
      <div className="App">
        <div>
          <h1>Search Conditions by Symptoms</h1>
          <>
            <div className="searchInput">
              <CreatableSelect
                components={components}
                inputValue={inputValue}
                isClearable
                isMulti
                menuIsOpen={false}
                onChange={this.handleChange}
                onInputChange={this.handleInputChange}
                onKeyDown={this.handleKeyDown}
                placeholder="Type HPO ID's and press enter..."
                value={selectedValues} />
            </div>
            <Button variant="contained" color="primary" onClick={() => this.searchConditions()}>Search</Button></>
          <Container>
            <Table data={conditions} />
          </Container>
        </div>
      </div>
    );
  }
}