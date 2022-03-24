import React, { forwardRef } from "react";
import MaterialTable, { Column, Icons } from "@material-table/core";
import {
    AddBox,
    ArrowDownward,
    Check,
    ChevronLeft,
    ChevronRight,
    Clear,
    DeleteOutline,
    Edit,
    FilterList,
    FirstPage,
    LastPage,
    Remove,
    SaveAlt,
    ViewColumn
} from "@material-ui/icons";
import { Container } from "@material-ui/core";
import { ColumnHeader, Condition } from "../type";

const tableIcons: Icons = {
    Add: forwardRef((props, ref) => <AddBox {...props} ref={ref} />),
    Check: forwardRef((props, ref) => <Check {...props} ref={ref} />),
    Clear: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
    Delete: forwardRef((props, ref) => <DeleteOutline {...props} ref={ref} />),
    DetailPanel: forwardRef((props, ref) => (
        <ChevronRight {...props} ref={ref} />
    )),
    Edit: forwardRef((props, ref) => <Edit {...props} ref={ref} />),
    Export: forwardRef((props, ref) => <SaveAlt {...props} ref={ref} />),
    Filter: forwardRef((props, ref) => <FilterList {...props} ref={ref} />),
    FirstPage: forwardRef((props, ref) => <FirstPage {...props} ref={ref} />),
    LastPage: forwardRef((props, ref) => <LastPage {...props} ref={ref} />),
    NextPage: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
    PreviousPage: forwardRef((props, ref) => (
        <ChevronLeft {...props} ref={ref} />
    )),
    SortArrow: forwardRef((props, ref) => <ArrowDownward {...props} ref={ref} />),
    ThirdStateCheck: forwardRef((props, ref) => <Remove {...props} ref={ref} />),
    ViewColumn: forwardRef((props, ref) => <ViewColumn {...props} ref={ref} />)
};

type Props = {
    data: Condition[];
};

const columns: Array<Column<ColumnHeader>> = [
    { title: "Orpha Code", field: "orpha_code" },
    { title: "Disease/Disorder", field: "name" }
];

const options = {
    paging: false,
    pageSize: 100,
    emptyRowsWhenPaging: false,
};

export const Table = ({ data }: Props) => {
    return (
        <Container>
            <MaterialTable
                style={{
                    marginTop: '15px'
                }}
                title=""
                columns={columns}
                data={data}
                icons={tableIcons}
                options={options}
            />
        </Container>
    );
};
