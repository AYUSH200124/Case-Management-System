import "./table.scss";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

const List = () => {
  const rows = [
    {
      id: 1143155,
      product: "Dog",
      img: "https://m.media-amazon.com/images/I/81bc8mA3nKL._AC_UY327_FMwebp_QL65_.jpg",
      customer: "Robin Raj",
      date: "1 March",
      amount: "Jamshedpur",
      method: "minor",
      status: "Approved",
    },
    {
      id: 2235235,
      product: "Cat",
      img: "https://m.media-amazon.com/images/I/31JaiPXYI8L._AC_UY327_FMwebp_QL65_.jpg",
      customer: "Vedant Alimchandani",
      date: "1 March",
      amount: "Delhi",
      method: "major",
      status: "Pending",
    },
    {
      id: 2342353,
      product: "Monkey",
      img: "https://m.media-amazon.com/images/I/71kr3WAj1FL._AC_UY327_FMwebp_QL65_.jpg",
      customer: "Anusheel Solanki",
      date: "1 March",
      amount: "Mumbai",
      method: "major",
      status: "Pending",
    },
    {
      id: 2357741,
      product: "Cow",
      img: "https://m.media-amazon.com/images/I/71wF7YDIQkL._AC_UY327_FMwebp_QL65_.jpg",
      customer: "Krisha Sanghvi",
      date: "1 March",
      amount: "Manali",
      method: "minor",
      status: "Approved",
    },
    {
      id: 2342355,
      product: "Snake",
      img: "https://m.media-amazon.com/images/I/81hH5vK-MCL._AC_UY327_FMwebp_QL65_.jpg",
      customer: "Naman Ajay Markhedkar",
      date: "1 March",
      amount: "Kasol",
      method: "minor",
      status: "Pending",
    },
  ];
  return (
    <TableContainer component={Paper} className="table">
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell className="tableCell">Case ID</TableCell>
            <TableCell className="tableCell">Animal Type</TableCell>
            <TableCell className="tableCell">Reporter</TableCell>
            <TableCell className="tableCell">Date</TableCell>
            <TableCell className="tableCell">Area</TableCell>
            <TableCell className="tableCell">Injury type</TableCell>
            <TableCell className="tableCell">Status</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell className="tableCell">{row.id}</TableCell>
              <TableCell className="tableCell">
                <div className="cellWrapper">
                  <img src={row.img} alt="" className="image" />
                  {row.product}
                </div>
              </TableCell>
              <TableCell className="tableCell">{row.customer}</TableCell>
              <TableCell className="tableCell">{row.date}</TableCell>
              <TableCell className="tableCell">{row.amount}</TableCell>
              <TableCell className="tableCell">{row.method}</TableCell>
              <TableCell className="tableCell">
                <span className={`status ${row.status}`}>{row.status}</span>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default List;
