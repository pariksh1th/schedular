/* eslint-disable react/no-unknown-property */

export default function InputTable({ clickRef }) {
  return (
    <>
      <label for="my-modal-6" ref={clickRef} className="btn modal-button">
        open modal
      </label>

      <input type="checkbox" id="my-modal-6" className="modal-toggle" />
      <div className="modal modal-bottom sm:modal-middle">
        <div className="modal-box">
          <h3 className="font-bold text-lg">Add Timetable!</h3>
          <p className="py-4">
            Youve been selected for a chance to get one year of subscription to
            use Wikipedia for free!
          </p>
          <div className="modal-action">
            <label for="my-modal-6" className="btn">
              Yay!
            </label>
          </div>
        </div>
      </div>
    </>
  );
}
