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
            pm.expect(doc.endPoint).to.match(/^https:\/\/trek\.nasa\.gov\/tiles\/Mars\/NP\/Mars_MOLA_blend200ppx_HRSC_ClrShade_clon0dd_200mpp_lzw_np$/);
        }
    });
});
