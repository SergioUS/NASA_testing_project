// Test 1: Validate status code (should be 200)
pm.test("Test 1: Verify that the status code is 200", function () {
    pm.response.to.have.status(200);
});
// Test 2: Validate the response time (should be less than 500)
pm.test("Test 2: Validate the response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
// Test 3: Validate the response size (should be less than 2KB)
pm.test("Test 3: Validate the response size is less than 2KB", function () {
    pm.expect(pm.response.responseTime).to.be.below(2000);
});
// Test 4: Verify the length of the response data
pm.test("Test 4: Verify the response data length must be greater than zero", function () {
    const responseData = pm.response.json();
    pm.expect(Object.keys(responseData.response).length).to.be.above(0, "Response data should not be empty");
});
// Test 5: Verify that each image URL in the response is valid
pm.test("Test 5: Verify that each image URL in the response is valid", function () {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    docs.forEach((doc) => {
        if (doc.endPoint) {
            pm.expect(doc.endPoint).to.match(/^https:\/\/[a-zA-Z0-9.-]+\/tiles\/Moon\/EQ\/Apollo15_MetricCam_ClrShade_Global_1024ppd$/);
        }
    });
});

// Test 6: Each serviceType in the response is valid
pm.test("Test 6: Each serviceType in the response is valid", function () {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    docs.forEach((doc) => {
        if (doc.serviceType) {
            pm.expect(doc.serviceType).to.match(/Mosaic|raster/);
        }
    });
});

// Test 7: Each protocol in the response is valid
pm.test("Test 7: Each protocol in the response is valid", function () {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    docs.forEach((doc) => {
        if (doc.protocol) {
            pm.expect(doc.protocol).to.match(/WMTS|ArcGISImageService/);
        }
    });
});
// Test 8:
pm.test("Test 8: Each item_UUID in the response is valid", function () {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    docs.forEach((doc) => {
        if (doc.item_UUID) {
            pm.expect(doc.item_UUID).to.match(/e546b0ab-b8d7-48da-bddd-e4d82f5f05b4/);
        }
    });
});
// Test 9:

pm.test("Test 9: Each item_DBID matches the expected DBID", function () {
    const responseData = pm.response.json();

    pm.expect(responseData.response.docs).to.be.an('array');

    responseData.response.docs.forEach(function(doc) {
        pm.expect(doc.item_DBID).to.equal(289724, 289720, 289733);
    });
});

// Test 10:
pm.test("Test 10: Each id in the response is valid", function () {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    docs.forEach((doc) => {
        if (doc.id) {
            pm.expect(doc.id).to.match(/eadf3412-6b26-4b3e-a9b9-74c3e942bda7/);
        }
    });
});
// Test 11:
pm.test("Test 11: Each _version_ in the response is valid", function () {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    docs.forEach((doc) => {
        if (doc._version_) {
            pm.expect(doc._version_).to.match(/1731216508059648000/);
        }
    });
});

// Test 12:

pm.test("Test 12: Each wmts_mode in the response is valid", function () {
    const responseData = pm.response.json();

    pm.expect(responseData.response.docs).to.be.an('array');
    responseData.response.docs.forEach(function(doc) {
        pm.expect(doc.wmts_mode).to.exist.and.to.be.oneOf(['rest', 'valid_value_2', 'valid_value_3']);
    });
});
// Test 13:

pm.test("Test 13: Response has the correct Content-Type header", function () {
    pm.expect(pm.response.headers.get("Content-Type")).to.include("application/json");
});

// .............................

pm.test("Test 14 ; Verify the presence of a specific error message in the response", function () {
    const responseData = pm.response.json();

    pm.expect(responseData).to.have.property('responseHeader');
    pm.expect(responseData.responseHeader).to.have.property('status', 0);
});

pm.test("Test 15: Verify the presence of the 'QTime' field in the response", function () {
    const responseData = pm.response.json();

    pm.expect(responseData).to.have.property('responseHeader');
    pm.expect(responseData.responseHeader).to.have.property('QTime', 0);
});

pm.test("Test 16: Verify response body contains expected 'numFound' value", function () {
    const responseData = pm.response.json();

    pm.expect(responseData).to.be.an('object');
    pm.expect(responseData.response.numFound).to.exist;
});

pm.test("Test 17: Verify the 'params.q' parameter is present and has a valid value", function () {
    const responseData = pm.response.json();
    pm.expect(responseData.responseHeader.params).to.have.property('q').that.is.a('string').and.to.have.lengthOf.above(0);
});
// Test to check if the params.version parameter is present and has a valid value
pm.test("Test 18: Params 'version' parameter is present and has a valid value", function() {
    const responseData = pm.response.json();
    pm.expect(responseData.responseHeader.params).to.have.property('version').that.is.a('string').and.to.have.lengthOf.above(0);
});
// Test to check if the params.wwt parameter is present and has a valid value
pm.test("Test 19: Verify 'params.wt' parameter is present and has a valid value", function() {
    const responseData = pm.response.json();
    const params = responseData.responseHeader.params; // Updated to access responseHeader instead of response

    pm.expect(params).to.have.property('wt').that.is.a('string').and.to.have.lengthOf.above(0);
});

// Test to check if the docs.layerId parameter is present and has a valid value
pm.test("Test 20: Verify docs 'layerId' parameter is present and has a valid value", function() {
    const responseData = pm.response.json();
    const docs = responseData.response.docs;

    docs.forEach((doc) => {
        pm.expect(doc).to.have.property('layerId').that.is.a('string').and.to.have.lengthOf.above(0);
    });
});

pm.test("Test 21: Verify response body contains expected 'start' value", function () {
    const responseData = pm.response.json();

    pm.expect(responseData).to.be.an('object');
    pm.expect(responseData.response.start).to.exist;
});

// Test 22: Verify response headers.
pm.test("Test 22: Verify the header keys are present", function () {
    pm.response.to.have.header("Date");
    pm.response.to.have.header("X-Frame-Options");
    pm.response.to.have.header("Server");
    pm.response.to.have.header("Strict-Transport-Security");
    pm.response.to.have.header("Access-Control-Allow-Origin");
    pm.response.to.have.header("Content-Security-Policy");
    pm.response.to.have.header("Keep-Alive");
    pm.response.to.have.header("Connection");
    pm.response.to.have.header("Transfer-Encoding");
});
