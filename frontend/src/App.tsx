import React, { Component, KeyboardEventHandler } from 'react';
import './App.css';
import axios from 'axios';

import CreatableSelect from 'react-select/creatable';
import { ActionMeta, OnChangeValue } from 'react-select';
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
  readonly value: readonly Option[];
  conditions: Condition[];
}
export default class App extends Component<{}, State> {
  state: State = {
    inputValue: '',
    value: [],
    conditions: [],
  };
  searchHPO = () => {
    const { value, conditions } = this.state;
    console.log(value);
    axios.post<Condition[]>('http://localhost:8000/api/diseases/', value).then(response => {
      console.log(response.data);
      this.setState({ conditions: response.data });
      console.log(conditions);
    });
  };
  handleChange = (
    value: OnChangeValue<Option, true>,
    actionMeta: ActionMeta<Option>
  ) => {
    console.group('Value Changed');
    console.log(value);
    console.log(`action: ${actionMeta.action}`);
    console.groupEnd();
    this.setState({ value });
  };
  handleInputChange = (inputValue: string) => {
    this.setState({ inputValue });
  };
  handleKeyDown: KeyboardEventHandler<HTMLDivElement> = (event) => {
    const { inputValue, value } = this.state;
    if (!inputValue) return;
    switch (event.key) {
      case 'Enter':
      case 'Tab':
        console.group('Value Added');
        console.log(value);
        console.groupEnd();
        this.setState({
          inputValue: '',
          value: [...value, createOption(inputValue)],
        });
        event.preventDefault();
    }
  };
  render() {
    const { inputValue, value, conditions } = this.state;
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
                value={value} />
            </div>
            <Button variant="contained" color="primary" onClick={() => this.searchHPO()}>Search</Button></>
          <Container>
            <Table data={conditions} />
          </Container>
        </div>
      </div>
    );
  }
}