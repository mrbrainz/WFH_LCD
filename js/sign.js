var url = window.location.href,
urlarr = url.split("/"),
root = urlarr[0] + "//" + urlarr[2] + "/api/",
dmp = console.log.bind(console),
statuses = [
    {
      name: "available",
      title: "Available"
    },
    {
      name: "busy",
      title: "Busy"
    },
    {
      name: "away",
      title: "Away"
    },
    {
      name: "meeting",
      title: "In A Meeting"
    },
    {
      name: "phone",
      title: "On The Phone"
    },
    {
      name: "email",
      title: "Sending Emails"
    },
    {
      name: "video",
      title: "On A Video Call"
    },
    {
      name: "dout",
      title: "Me Time"
    },
    {
      name: "clear",
      title: "Clear Status Screen"
    }
];

function formatAMPM(date) {
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? 'pm' : 'am';
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  minutes = minutes < 10 ? '0'+minutes : minutes;
  var strTime = hours + ':' + minutes + ' ' + ampm;
  return strTime;
}

function aGet(url, cb) {
    var x = new XMLHttpRequest();
    x.onload = function(e) {
        if (x.status != 200) {
          setErrorState();
          cb(x);
        } else {
          unlockForLoading();
        }
        return;
    };
    x.onerror= function(e) {
        setErrorState();
        cb(e);
        return;
    };
    x.open("GET", url, true);
    x.send();
    return;
}

function getStatusTitle(status) {
  var obj = filterObjByName(statuses, status);
  if (!obj.length) {
    return false;
  }
  return obj[0].title;
}

function filterObjByName(jsObjects,value) {
  var result = jsObjects.filter(obj => {
    return obj.name === value
  });
  return result;
}

function setTitle(title) {
  document.getElementById("last-status-title").innerText = title;
  document.getElementById("last-status-time").innerText = formatAMPM(new Date);
}

function setErrorState() {
  deactiveAnyButton();
  setTitle("Update Error");
  document.getElementById("last-status").classList.add("error");
  unlockForLoading();
}

function clearErrorState() {
  document.getElementById("last-status").classList.remove("error");
}

function changeStatus(status) {
  clearErrorState();
  deactiveAnyButton();
  var title = getStatusTitle(status);
  if (!title) {
    alert('"'+ status + '" is not a defined status');
    setErrorState();
    return false;
  } else {
    lockForLoading();
    setTitle(title);
    activateButton(status);
    aGet(root+status, dmp);
  }
}

function activateButton(status) {
  var button = document.getElementById("action-"+status);
  button.classList.add("active");
}

function deactiveAnyButton() {
  var buttons = document.getElementsByClassName("active");
  for (var i=0;i<buttons.length;i++) {
    buttons[i].classList.remove("active");
  }
}

function lockForLoading() {
  document.getElementsByTagName("body")[0].classList.add("loading");
}

function unlockForLoading() {
  document.getElementsByTagName("body")[0].classList.remove("loading");
}

function createButtonGrid() {
  var grid = document.createElement("ul");
  grid.id = "button-grid";
  grid.className = "row";

  for (var i=0;i<statuses.length;i++) {
    var li = document.createElement("li");
    li.className = "button col-xl-3 col-lg-3 col-md-4 col-sm-6 col-6";

    var button = document.createElement("button");
    button.className = "action-button btn btn-outline-primary btn-lg btn-block";
    button.id = "action-"+statuses[i].name;
    button.innerText = statuses[i].title;
    button.type = "button";

    li.appendChild(button);
    grid.appendChild(li);

  }

  var container = document.getElementById("control-grid");
  container.appendChild(grid);

}

function makeButtonsClick() {
  var elements = document.getElementsByClassName('action-button');
   for(var i = 0; i < elements.length; i++){
      elements[i].onclick = function() {
        if (!document.getElementsByTagName("body")[0].classList.contains("loading")) {
          changeStatus(this.id.replace("action-",""));
        }
      };
   }
}

createButtonGrid();
makeButtonsClick();
unlockForLoading();
