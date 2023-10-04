/**
 * Send a request to aws, the request is controled by the url
 * @param {*} name Instance name
 * @param {*} url Url defined by django.
 * @returns The json data returned by django.
 */
const request_ec2_by_name = async (name, url) => {
  console.log(`${url}/${name}`);
  const json_data = await fetch(`${url}/${name}`).then((response) =>
    response.json()
  );
  return json_data;
};

/**
 * Displays instance info in the page
 * @param {*} data Json data of instance info
 */
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
