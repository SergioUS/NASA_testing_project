// Test 1: Validate status code (should be 200)
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
// Test 2: Validate the response time (should be less than 500)
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
// Test 3: Validate the response size (should be less than 2KB)
pm.test("Response size is less than 2KB", function () {
    pm.expect(pm.response.responseTime).to.be.below(2000);
});
// Test 4: Verify the length of the response data
pm.test("The response data length must be greater than zero", function () {
    const responseData = pm.response.json();
    pm.expect(Object.keys(responseData.response).length).to.be.above(0, "Response data should not be empty");
});
// Test 5: Verify that each image URL in the response is valid
pm.test("Each image URL in the response is valid", function () {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    // Check each image URL in the response
    docs.forEach((doc) => {
        if (doc.endPoint) {
            pm.expect(doc.endPoint).to.match(/^https:\/\/trek\.nasa\.gov\/tiles\/Mars\/NP\/Mars_MO_THEMIS-IR-Day_mosaic_global_100m_v12_clon0_ly_np$/);
        }
    });
});

// Test 6:
pm.test("Each serviceType in the response is valid", function () {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    docs.forEach((doc) => {
        if (doc.serviceType) {
            pm.expect(doc.serviceType).to.match(/Mosaic|raster/);
        }
    });
});

// Test 7:
pm.test("Each protocol in the response is valid", function () {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    docs.forEach((doc) => {
        if (doc.protocol) {
            pm.expect(doc.protocol).to.match(/WMTS|ArcGISImageService/);
        }
    });
});
// Test 8:
pm.test("Each item_UUID in the response is valid", function () {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    docs.forEach((doc) => {
        if (doc.item_UUID) {
            pm.expect(doc.item_UUID).to.match(/866bbddf-f40d-4377-8828-124e56c037eb/);
        }
    });
});
// Test 9:
pm.test("Each item_DBID in the response is valid", function () {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    docs.forEach((doc) => {
        if (doc.item_DBID) {
            pm.expect(doc.item_DBID).to.match(/293972/);
        }
    });
});
// Test 10:
pm.test("Each id in the response is valid", function () {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    docs.forEach((doc) => {
        if (doc.id) {
            pm.expect(doc.id).to.match(/533f6bcb-e675-41c3-93a6-7d73c6ee44c7/);
        }
    });
});
// Test 11:
pm.test("Each _version_ in the response is valid", function () {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    docs.forEach((doc) => {
        if (doc._version_) {
            pm.expect(doc._version_).to.match(/1673572476374745088/);
        }
    });
});
