export const userColumns = [
  { field: "id", headerName: "Case ID", width: 70 },
  {
    field: "user",
    headerName: "Animal",
    width: 230,
    renderCell: (params) => {
      return (
        <div className="cellWithImg">
          <img className="cellImg" src={params.row.img} alt="avatar" />
          {params.row.username}
        </div>
      );
    },
  },
  {
    field: "email",
    headerName: "Address",
    width: 230,
  },

  {
    field: "age",
    headerName: "Reporters Phone number",
    width: 100,
  },
  {
    field: "status",
    headerName: "Status",
    width: 160,
    renderCell: (params) => {
      return (
        <div className={`cellWithStatus ${params.row.status}`}>
          {params.row.status}
        </div>
      );
    },
  },
];

//temporary data
/*export const userRows = [
  {
    id: 1,
    username: "Dog",
    img: "https://media-exp2.licdn.com/dms/image/C560BAQF4QkCI3LrGWw/company-logo_200_200/0/1644231762697?e=2147483647&v=beta&t=psmxcZwe7VpV1ijOBFD5Vb-ewU90uG1ByP90e0Jk2vo",
    status: "active",
    email: "1snow@gmail.com",
    age: 9204383793,
  },
  {
    id: 2,
    username: "Cat",
    img: "https://media-exp2.licdn.com/dms/image/C560BAQF4QkCI3LrGWw/company-logo_200_200/0/1644231762697?e=2147483647&v=beta&t=psmxcZwe7VpV1ijOBFD5Vb-ewU90uG1ByP90e0Jk2vo",
    email: "2snow@gmail.com",
    status: "pending",
    age: 9204383793,
  },
  {
    id: 3,
    username: "Cute Dog",
    img: "https://media-exp2.licdn.com/dms/image/C560BAQF4QkCI3LrGWw/company-logo_200_200/0/1644231762697?e=2147483647&v=beta&t=psmxcZwe7VpV1ijOBFD5Vb-ewU90uG1ByP90e0Jk2vo",
    email: "3snow@gmail.com",
    status: "pending",
    age: 9204383793,
  },
  {
    id: 4,
    username: "Cute cat",
    img: "https://media-exp2.licdn.com/dms/image/C560BAQF4QkCI3LrGWw/company-logo_200_200/0/1644231762697?e=2147483647&v=beta&t=psmxcZwe7VpV1ijOBFD5Vb-ewU90uG1ByP90e0Jk2vo",
    email: "4snow@gmail.com",
    status: "active",
    age: 9204383793,
  },
  {
    id: 5,
    username: "more animals",
    img: "https://media-exp2.licdn.com/dms/image/C560BAQF4QkCI3LrGWw/company-logo_200_200/0/1644231762697?e=2147483647&v=beta&t=psmxcZwe7VpV1ijOBFD5Vb-ewU90uG1ByP90e0Jk2vo",
    email: "5snow@gmail.com",
    status: "Complete",
    age: 9204383793,
  },
  {
    id: 6,
    username: "even more animals",
    img: "https://media-exp2.licdn.com/dms/image/C560BAQF4QkCI3LrGWw/company-logo_200_200/0/1644231762697?e=2147483647&v=beta&t=psmxcZwe7VpV1ijOBFD5Vb-ewU90uG1ByP90e0Jk2vo",
    email: "6snow@gmail.com",
    status: "pending",
    age: 9204383793,
  },
  {
    id: 7,
    username: "stupid monkey",
    img: "https://media-exp2.licdn.com/dms/image/C560BAQF4QkCI3LrGWw/company-logo_200_200/0/1644231762697?e=2147483647&v=beta&t=psmxcZwe7VpV1ijOBFD5Vb-ewU90uG1ByP90e0Jk2vo",
    email: "7snow@gmail.com",
    status: "pending",
    age: 9204383793,
  },
  {
    id: 8,
    username: "Fish maybe",
    img: "https://media-exp2.licdn.com/dms/image/C560BAQF4QkCI3LrGWw/company-logo_200_200/0/1644231762697?e=2147483647&v=beta&t=psmxcZwe7VpV1ijOBFD5Vb-ewU90uG1ByP90e0Jk2vo",
    email: "8snow@gmail.com",
    status: "Complete",
    age: 9204383793,
  },
  {
    id: 9,
    username: "cute cat",
    img: "https://media-exp2.licdn.com/dms/image/C560BAQF4QkCI3LrGWw/company-logo_200_200/0/1644231762697?e=2147483647&v=beta&t=psmxcZwe7VpV1ijOBFD5Vb-ewU90uG1ByP90e0Jk2vo",
    email: "Jamshedpur",
    status: "pending",
    age: 9204383793,
  },
  {
    id: 10,
    username: "cute dog",
    img: "https://media-exp2.licdn.com/dms/image/C560BAQF4QkCI3LrGWw/company-logo_200_200/0/1644231762697?e=2147483647&v=beta&t=psmxcZwe7VpV1ijOBFD5Vb-ewU90uG1ByP90e0Jk2vo",
    email: "Jamshedpur",
    status: "active",
    age: 9204383793,
  },
];
*/
