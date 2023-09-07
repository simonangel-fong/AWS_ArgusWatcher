// window.location.host

const fetch_ec2_by_name = async (name, url = INFO_URL) => {
  const json_data = await fetch(`${url}/${name}`).then((response) =>
    response.json()
  );
  return json_data;
};

function display(data) {
  if (data["status"] == "success") {
    data = JSON.parse(data["data"])[0];
    console.log(data);
    $("#instance_id").text(data["instance_id"]);
    if (data["public_ip"]) {
      $("#public_ip").html(
        `<a href="http://${data["public_ip"]}" target="_blank">${data["public_ip"]}</a>`
      );
    }
    $("#status").text(data["status"]);
    if (data["status"] == "running") {
      $("#status").addClass("text-success");
    }
  } else {
    $("#status").addClass("text-secondary");
  }
}

// fetch_ec2_by_name("ArgusWatcher", UPDATE_CODE_URL).then((data) =>
//   console.log(data)
// );
