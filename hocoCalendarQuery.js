var ret = jQuery('#calendar').fullCalendar({
    year: "2022",
    month: "6",
    theme: true,
    defaultView: "month",
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'month,basicWeek,basicDay'
    },
    viewDisplay: function (element) {
    UpdateDropDownFilters();
    },
    editable: false,
    events: "/desktopmodules/EventPlannerModule/EventPlannerHandler.ashx?alias=cc.howardcountymd.gov&moduleId=6675&portalId=0&action=get_events_by_date&tabModuleId=3702&tabId=493"
});